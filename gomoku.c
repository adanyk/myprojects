#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define SIZE 15   //board size
#define DEPTH 5   //search depth
#define STREAK 5  //how many x/o in a row is required to win


struct board
{
    char fields[SIZE][SIZE], turn;
};

struct board start()
{
    struct board b;
    for(int i = 0; i - SIZE; i++)
        for(int j = 0; j - SIZE; b.fields[i][j++] = '.')
    b.turn = 'o';
    return b;
}

void displayboard(struct board *b)
{
    printf("    ");
    for(int i = 0; i - SIZE; printf("%3d", ++i));
    for(int i = 0; i - SIZE; i++)
    {
        printf("\n");
        printf("%3d ", i + 1);
        for(int j = 0; j - SIZE; printf("%3c", b->fields[i][j++]));
    }
    printf("\n\n");
}

int evaluate(struct board *b)
{
    // -10000: o won
    //  10000: x won
    //      0: tie

    int x = 0, o = 0;
    for(int i = 0; i - SIZE; i++)
    {
        for(int j = 0; j - SIZE; j++)
        {
            if(b->fields[i][j] == 'x')
            {
                x++;
                if(x == STREAK)  return 10000;
                o = 0;
            }
            else if(b->fields[i][j] == 'o')
            {
                o++;
                if(o == STREAK)  return -10000;
                x = 0;
            }
            else
            {
                x = 0;
                o = 0;
            }
        }
        x = 0;
        o = 0;
    }

    for(int i = 0; i - SIZE; i++)
    {
        for(int j = 0; j - SIZE; j++)
        {
            if(b->fields[j][i] == 'x')
            {
                x++;
                if(x == STREAK)  return 10000;
                o = 0;
            }
            else if(b->fields[j][i] == 'o')
            {
                o++;
                if(o == STREAK)  return -10000;
                x = 0;
            }
            else
            {
                x = 0;
                o = 0;
            }
        }
        x = 0;
        o = 0;
    }

    for(int i = STREAK - 1; i - 2 * SIZE + STREAK; i++)
    {
        if(i < SIZE)
        {
            for(int j = 0; j - i - 1; j++)
            {
                if(b->fields[i - j][j] == 'x')
                {
                    x++;
                    if(x == STREAK)  return 10000;
                    o = 0;
                }
                else if(b->fields[i - j][j] == 'o')
                {
                    o++;
                    if(o == STREAK)  return -10000;
                    x = 0;
                }
                else
                {
                    x = 0;
                    o = 0;
                }
            }
        }
        else
        {
            for(int j = 0; j - 2 * SIZE + i + 1; j++)
            {
                if(b->fields[SIZE - j - 1][i - SIZE + 1 + j] == 'x')
                {
                    x++;
                    if(x == STREAK)  return 10000;
                    o = 0;
                }
                else if(b->fields[SIZE - j - 1][i - SIZE + 1 + j] == 'o')
                {
                    o++;
                    if(o == STREAK)  return -10000;
                    x = 0;
                }
                else
                {
                    x = 0;
                    o = 0;
                }
            }
        }
        x = 0;
        o = 0;     
    }

    for(int i = STREAK - 1; i - 2 * SIZE + STREAK; i++)
    {
        if(i < SIZE)
        {
            for(int j = 0; j - i - 1; j++)
            {
                if(b->fields[SIZE - 1 - i + j][j] == 'x')
                {
                    x++;
                    if(x == STREAK)  return 10000;
                    o = 0;
                }
                else if(b->fields[SIZE - 1 - i + j][j] == 'o')
                {
                    o++;
                    if(o == STREAK)  return -10000;
                    x = 0;
                }
                else
                {
                    x = 0;
                    o = 0;
                }
            }
        }
        else
        {
            for(int j = 0; j - 2 * SIZE + i + 1; j++)
            {
                if(b->fields[j][i - SIZE + 1 + j] == 'x')
                {
                    x++;
                    if(x == STREAK)  return 10000;
                    o = 0;
                }
                else if(b->fields[j][i - SIZE + 1 + j] == 'o')
                {
                    o++;
                    if(o == STREAK)  return -10000;
                    x = 0;
                }
                else
                {
                    x = 0;
                    o = 0;
                }
            }
        }
        x = 0;
        o = 0;     
    }
    return 0;
}

int evaluate_precisely(struct board *b)
{
    //  10000: x won
    // -10000: o won
    // every n*x in a line: +n^3
    // every n*o in a line: -n^3

    int x = 0, o = 0, not_x = 0, not_o = 0, evaluate = 0;
    char last = '.';
    for(int i = 0; i - SIZE; i++)
    {
        for(int j = 0; j - SIZE; j++)
        {
            if(b->fields[i][j] == '.')
            {
                not_x++;
                not_o++;
            }
            else if(b->fields[i][j] == 'x')
            {
                x++;
                not_o++;
                not_x = 0;
                o = 0;
                last = 'x';
            }
            else
            {
                o++;
                not_x++;
                not_o = 0;
                x = 0;
                last = 'o';
            }

            if(not_o >= STREAK && last == 'x')
            {
                if(j > STREAK - 1 && b->fields[i][j - STREAK] == 'x')   x--;
                if(x == STREAK)  return 10000;
                if(b->fields[i][j] == 'x' && j < SIZE - 1 && b->fields[i][j + 1] == 'x');
                else    evaluate += x * x * x;
            }
            else if(not_x >= STREAK && last == 'o')
            {
                if(j > STREAK - 1 && b->fields[i][j - STREAK] == 'o')   o--;
                if(o == STREAK)  return -10000;
                if(b->fields[i][j] == 'o' && j < SIZE - 1 && b->fields[i][j + 1] == 'o');
                else    evaluate -= o * o * o;
            }
        }
        x = 0;
        o = 0;
        not_x = 0;
        not_o = 0;
        last = '.';
    }

    for(int i = 0; i - SIZE; i++)
    {
        for(int j = 0; j - SIZE; j++)
        {
            if(b->fields[j][i] == '.')
            {
                not_x++;
                not_o++;
            }
            else if(b->fields[j][i] == 'x')
            {
                x++;
                not_o++;
                not_x = 0;
                o = 0;
                last = 'x';
            }
            else
            {
                o++;
                not_x++;
                not_o = 0;
                x = 0;
                last = 'o';
            }

            if(not_o >= STREAK && last == 'x')
            {
                if(j > STREAK - 1 && b->fields[j - STREAK][i] == 'x')   x--;
                if(x == STREAK)  return 10000;
                if(b->fields[j][i] == 'x' && j < SIZE - 1 && b->fields[j + 1][i] == 'x');
                else    evaluate += x * x * x;
            }
            else if(not_x >= STREAK && last == 'o')
            {
                if(j > STREAK - 1 && b->fields[j - STREAK][i] == 'o')   o--;
                if(o == STREAK)  return -10000;
                if(b->fields[j][i] == 'o' && j < SIZE - 1 && b->fields[j + 1][i] == 'o');
                else    evaluate -= o * o * o;
            }
        }
        x = 0;
        o = 0;
        not_x = 0;
        not_o = 0;
        last = '.';
    }

    for(int i = STREAK - 1; i - 2 * SIZE + STREAK; i++)
    {
        if(i < SIZE)
        {
            for(int j = 0; j - i - 1; j++)
            {
                if(b->fields[i - j][j] == '.')
                {
                    not_x++;
                    not_o++;
                }
                else if(b->fields[i - j][j] == 'x')
                {
                    x++;
                    not_o++;
                    not_x = 0;
                    o = 0;
                    last = 'x';
                }
                else
                {
                    o++;
                    not_x++;
                    not_o = 0;
                    x = 0;
                    last = 'o';
                }

                if(not_o >= STREAK && last == 'x')
                {
                    if(j > STREAK - 1 && b->fields[i - j + STREAK][j - STREAK] == 'x')   x--;
                    if(x == STREAK)  return 10000;
                    if(b->fields[i - j][j] == 'x' && j < (j - i - 1) - 1 && b->fields[i - j - 1][j + 1] == 'x');
                    else    evaluate += x * x * x;
                }
                else if(not_x >= STREAK && last == 'o')
                {
                    if(j > STREAK - 1 && b->fields[i - j + STREAK][j - STREAK] == 'o')   o--;
                    if(o == STREAK)  return -10000;
                    if(b->fields[i - j][j] == 'o' && j < (j - i - 1) - 1 && b->fields[i - j - 1][j + 1] == 'o');
                    else    evaluate -= o * o * o;
                }
            }
            x = 0;
            o = 0;
            not_x = 0;
            not_o = 0;
            last = '.';
        }
        else
        {
            
            for(int j = 0; j - 2 * SIZE + i + 1; j++)
            {
                if(b->fields[SIZE - j - 1][i - SIZE + 1 + j] == '.')
                {
                    not_x++;
                    not_o++;
                }
                else if(b->fields[SIZE - j - 1][i - SIZE + 1 + j] == 'x')
                {
                    x++;
                    not_o++;
                    not_x = 0;
                    o = 0;
                    last = 'x';
                }
                else
                {
                    o++;
                    not_x++;
                    not_o = 0;
                    x = 0;
                    last = 'o';
                }

                if(not_o >= STREAK && last == 'x')
                {
                    if(j > STREAK - 1 && b->fields[SIZE - j - 1 + STREAK][i - SIZE + 1 + j - STREAK] == 'x')   x--;
                    if(x == STREAK)  return 10000;
                    if(b->fields[SIZE - j - 1][i - SIZE + 1 + j] == 'x' && j < (j - 2 * SIZE + i + 1) - 1 && b->fields[(SIZE - j - 1) - 1][(i - SIZE + 1 + j) + 1] == 'x');
                    else    evaluate += x * x * x;
                }
                else if(not_x >= STREAK && last == 'o')
                {
                    if(j > STREAK - 1 && b->fields[SIZE - j - 1 + STREAK][i - SIZE + 1 + j - STREAK] == 'o')   o--;
                    if(o == STREAK)  return -10000;
                    if(b->fields[SIZE - j - 1][i - SIZE + 1 + j] == 'o' && j < (j - 2 * SIZE + i + 1) - 1 && b->fields[(SIZE - j - 1) - 1][(i - SIZE + 1 + j) + 1] == 'o');
                    else    evaluate -= o * o * o;
                }
            }
            x = 0;
            o = 0;
            not_x = 0;
            not_o = 0;
            last = '.';
        }
    }

    for(int i = STREAK - 1; i - 2 * SIZE + STREAK; i++)
    {
        if(i < SIZE)
        {
            for(int j = 0; j - i - 1; j++)
            {
                if(b->fields[SIZE - 1 - i + j][j] == '.')
                {
                    not_x++;
                    not_o++;
                }
                else if(b->fields[SIZE - 1 - i + j][j] == 'x')
                {
                    x++;
                    not_o++;
                    not_x = 0;
                    o = 0;
                    last = 'x';
                }
                else
                {
                    o++;
                    not_x++;
                    not_o = 0;
                    x = 0;
                    last = 'o';
                }

                if(not_o >= STREAK && last == 'x')
                {
                    if(j > STREAK - 1 && b->fields[(SIZE - 1 - i + j) - STREAK][j - STREAK] == 'x')   x--;
                    if(x == STREAK)  return 10000;
                    if(b->fields[SIZE - 1 - i + j][j] == 'x' && j < (j - i - 1) - 1 && b->fields[(SIZE - 1 - i + j) + 1][j + 1] == 'x');
                    else    evaluate += x * x * x;
                }
                else if(not_x >= STREAK && last == 'o')
                {
                    if(j > STREAK - 1 && b->fields[(SIZE - 1 - i + j) - STREAK][j - STREAK] == 'o')   o--;
                    if(o == STREAK)  return -10000;
                    if(b->fields[SIZE - 1 - i + j][j] == 'o' && j < (j - i - 1) - 1 && b->fields[(SIZE - 1 - i + j) + 1][j + 1] == 'o');
                    else    evaluate += o * o * o;
                }
            }
            x = 0;
            o = 0;
            not_x = 0;
            not_o = 0;
            last = '.';
        }
        else
        {
            for(int j = 0; j - 2 * SIZE + i + 1; j++)
            {
                if(b->fields[j][i - SIZE + 1 + j] == '.')
                {
                    not_x++;
                    not_o++;
                }
                else if(b->fields[j][i - SIZE + 1 + j] == 'x')
                {
                    x++;
                    not_o++;
                    not_x = 0;
                    o = 0;
                    last = 'x';
                }
                else
                {
                    o++;
                    not_x++;
                    not_o = 0;
                    x = 0;
                    last = 'o';
                }

                if(not_o >= STREAK && last == 'x')
                {
                    if(j > STREAK - 1 && b->fields[j - STREAK][(i - SIZE + 1 + j) - STREAK] == 'x')   x--;
                    if(x == STREAK)  return 10000;
                    if(b->fields[j][i - SIZE + 1 + j] == 'x' && j < (j - 2 * SIZE + i + 1) - 1 && b->fields[j + 1][(i - SIZE + 1 + j) + 1] == 'x');
                    else    evaluate += x * x * x;
                }
                else if(not_x >= STREAK && last == 'o')
                {
                    if(j > STREAK - 1 && b->fields[j - STREAK][(i - SIZE + 1 + j) - STREAK] == 'o')   o--;
                    if(o == STREAK)  return -10000;
                    if(b->fields[j][i - SIZE + 1 + j] == 'o' && j < (j - 2 * SIZE + i + 1) - 1 && b->fields[j + 1][(i - SIZE + 1 + j) + 1] == 'o');
                    else    evaluate += o * o * o;
                }
            }
            x = 0;
            o = 0;
            not_x = 0;
            not_o = 0;
            last = '.';
        }
    }
    return evaluate;
}



struct oneMove
{
    int row, col;
};

struct listOfMoves
{
    struct oneMove oM;
    struct listOfMoves* nxt;
};

struct listOfMoves* addMove(struct listOfMoves* h, int r, int c)
{
    struct listOfMoves *ptr = (struct listOfMoves*) calloc(1, sizeof(struct listOfMoves));
    ptr->oM.row = r;
    ptr->oM.col = c;
    ptr->nxt = NULL;
    if(h)
    {
        while(h->nxt)
            h = h->nxt;
        h->nxt = ptr;
    }
    return ptr;
}


struct listOfMoves* possibleMoves(struct board* b)//uses when basic
{
    struct listOfMoves *head = NULL;
    int first = 0;
    for(int i = 0; i - SIZE; i++)
    {
        for(int j = 0; j - SIZE; j++)
        {
            if(b->fields[i][j] == '.')
            {
                if(!first)
                {
                    head = addMove(NULL, i, j);
                    first++;
                }
                else   addMove(head, i, j);
            }
        }
    }
    return head;
}

struct listOfMoves* reduced(struct board* b)//uses when advanced
{
    int left = SIZE, right = 0, up = SIZE, down = 0;
    char UP = 'i', LEFT = 'i';
    for(int i = 0; i - SIZE; i++)
    {
        for(int j = 0; j - SIZE; j++)
        {
            if(b->fields[i][j] != '.')
            {
                if(UP == 'i')
                {
                    up = i;
                    UP = 'c';
                    down = i;
                }
                else if(down < i)   down = i;
                if(LEFT == 'i')
                {
                    left = j;
                    LEFT = 'c';
                    right = j;
                }
                else
                {
                    if(left > j)   left = j;
                    if(right < j)  right = j;
                }
            }
        }
    }
    if(up > 0)  up--;
    if(down < SIZE - 1) down++;
    if(left > 0)  left--;
    if(right < SIZE - 1) right++;
    
    struct listOfMoves *head = NULL;
    int first = 0;
    for(int i = up; i - down - 1; i++)
    {
        for(int j = left; j - right - 1; j++)
        {
            if(b->fields[i][j] == '.')
            {
                if(!first)
                {
                    head = addMove(NULL, i, j);
                    first++;
                }
                else   addMove(head, i, j);
            }
        }
    }
    return head;
}


void destroyList(struct listOfMoves* h)
{
    if(h)
    {
        if(h->nxt)
            destroyList(h->nxt);
        free(h);
    }
}

struct listOfMoves* deleteFirstMove(struct listOfMoves* head)
{
    struct listOfMoves *newHead = head->nxt;
    free(head);
    return newHead;
}

struct board makeMove(struct board b, struct oneMove oM)
{
    b.fields[oM.row][oM.col] = b.turn;
    if(b.turn == 'o')  b.turn = 'x';
    else               b.turn = 'o';
    return b;
}

int anyMovesLeft(struct board *b)
{
    for(int i = 0; i - SIZE; i++)
        for(int j = 0; j - SIZE; j++)
            if(b->fields[i][j] == '.')  return 1;
    return 0;
}



int alphabeta(struct board* b, int depth, int alpha, int beta)//uses when advanced
{
    if(depth == 0 || anyMovesLeft(b) == 0)  return evaluate_precisely(b);
    else if(b->turn == 'o' && evaluate(b) == 10000)   return 10000 + depth;
    else if(b->turn == 'x' && evaluate(b) == -10000)  return -10000 - depth;
    
    else if(depth == DEPTH)
    {
        //struct listOfMoves *list = possibleMoves(b);
        struct listOfMoves *list = reduced(b);
        int temp, value;
        struct board computerMove = makeMove(*b, list->oM);
        value = -10000;
        while(list)
        {
            struct board b2 = makeMove(*b, list->oM);
            list = deleteFirstMove(list);
            temp = alphabeta(&b2, depth - 1, alpha, beta);
            if(temp > value)
            {
                value = temp;
                computerMove = b2;
            }
            if(value > alpha)   alpha = value;
            if(beta <= alpha)
            {
                destroyList(list);
                break;
            }
        }
        *b = computerMove;
        return value;
    }
    else
    {        
        //struct listOfMoves *list = possibleMoves(b);
        struct listOfMoves *list = reduced(b);
        int temp, value;        
        if(b->turn == 'x')
        {
            value = -10000 + DEPTH;
            while(list)
            {
                struct board b2 = makeMove(*b, list->oM);
                list = deleteFirstMove(list);
                temp = alphabeta(&b2, depth - 1, alpha, beta);
                if(temp > value)    value = temp;
                if(value > alpha)   alpha = value;
                if(beta <= alpha)
                {
                    destroyList(list);
                    break;
                }
            }
        }
        else
        {
            value = 10000;
            while(list)
            {
                struct board b2 = makeMove(*b, list->oM);
                list = deleteFirstMove(list);
                temp = alphabeta(&b2, depth - 1, alpha, beta);
                if(temp < value)    value = temp;
                if(value < beta)   beta = value;
                if(beta <= alpha)
                {
                    destroyList(list);
                    break;
                }
            }
        }
        return value;
    }
}

int alphabeta_basic(struct board* b, int depth, int alpha, int beta)//uses when basic
{
    if(depth == 0 || anyMovesLeft(b) == 0)  return evaluate(b);
    else if(b->turn == 'o' && evaluate(b) == 10000)   return 10000 + depth;
    else if(b->turn == 'x' && evaluate(b) == -10000)  return -10000 - depth;
    
    else if(depth == DEPTH)
    {
        struct listOfMoves *list = possibleMoves(b);
        //struct listOfMoves *list = reduced(b);
        int temp, value;
        struct board computerMove = makeMove(*b, list->oM);
        value = -10000;
        while(list)
        {
            struct board b2 = makeMove(*b, list->oM);
            list = deleteFirstMove(list);
            temp = alphabeta_basic(&b2, depth - 1, alpha, beta);
            if(temp > value)
            {
                value = temp;
                computerMove = b2;
            }
            if(value > alpha)   alpha = value;
            if(beta <= alpha)
            {
                destroyList(list);
                break;
            }
        }
        *b = computerMove;
        return value;
    }
    else
    {        
        struct listOfMoves *list = possibleMoves(b);
        //struct listOfMoves *list = reduced(b);
        int temp, value;        
        if(b->turn == 'x')
        {
            value = -10000 + DEPTH;
            while(list)
            {
                struct board b2 = makeMove(*b, list->oM);
                list = deleteFirstMove(list);
                temp = alphabeta_basic(&b2, depth - 1, alpha, beta);
                if(temp > value)    value = temp;
                if(value > alpha)   alpha = value;
                if(beta <= alpha)
                {
                    destroyList(list);
                    break;
                }
            }
        }
        else
        {
            value = 10000;
            while(list)
            {
                struct board b2 = makeMove(*b, list->oM);
                list = deleteFirstMove(list);
                temp = alphabeta_basic(&b2, depth - 1, alpha, beta);
                if(temp < value)    value = temp;
                if(value < beta)   beta = value;
                if(beta <= alpha)
                {
                    destroyList(list);
                    break;
                }
            }
        }
        return value;
    }
}



void main(void)//advanced
{
    struct board b1 = start();
    displayboard(&b1);

    //player vs bot
    while(anyMovesLeft(&b1) && evaluate(&b1) != 10000)
    {
        struct oneMove playerMove;
        int validMove = 0, row, col, eval;
        do
        {
        printf("Your turn, type a valid move: \n");
        scanf("%d %d", &row, &col);
        if(b1.fields[row - 1][col - 1] == '.')   validMove = 1;
        }
        while(!validMove);
        playerMove.row = row - 1;
        playerMove.col = col - 1;
        b1 = makeMove(b1, playerMove);
        displayboard(&b1);
        clock_t start = clock();
        if(anyMovesLeft(&b1) && evaluate(&b1) != -10000)
        {
            eval = alphabeta(&b1, DEPTH, -10000, 10000);
            printf("\nEvaluate: %d\n\n", eval);
        }
        else
        {
            displayboard(&b1);
            break;
        }
        displayboard(&b1);
        clock_t stop = clock();
        int t = (stop - start)/1000000;
        printf("Time: %d\n", t);
    }

    //bot vs bot
    /*while(anyMovesLeft(&b1) && evaluate(&b1) != 10000)
    {
        int eval;
        
        clock_t start1 = clock();
        if(anyMovesLeft(&b1) && evaluate(&b1) != 10000)
        {
            eval = alphabeta(&b1, DEPTH, -10000, 10000);
            printf("\nEvaluate: %d\n\n", eval);
        }
        else
        {
            displayboard(&b1);
            break;
        }
        displayboard(&b1);
        clock_t stop1 = clock();
        int t1 = (stop1 - start1)/1000000;
        printf("Time: %d\n", t1);

        clock_t start = clock();
        if(anyMovesLeft(&b1) && evaluate(&b1) != -10000)
        {
            eval = alphabeta(&b1, DEPTH, -10000, 10000);
            printf("\nEvaluate: %d\n\n", eval);
        }
        else
        {
            displayboard(&b1);
            break;
        }
        displayboard(&b1);
        clock_t stop = clock();
        int t = (stop - start)/1000000;
        printf("Time: %d\n", t);
    }*/

    if(evaluate(&b1) == 10000)   printf("You lost!\n\n");
    else if(evaluate(&b1) == -10000)  printf("You won!\n\n");
}

/*void main(void)//basic
{
    struct board b1 = start();    
    b1.fields[1][1] = 'x';    
    displayboard(&b1);

    //player vs bot
    while(anyMovesLeft(&b1) && evaluate(&b1) != 10000)
    {
        struct oneMove playerMove;
        int validMove = 0, row, col, eval;
        do
        {
        printf("Your turn, type a valid move: \n");
        scanf("%d %d", &row, &col);
        if(b1.fields[row - 1][col - 1] == '.')   validMove = 1;
        }
        while(!validMove);
        playerMove.row = row - 1;
        playerMove.col = col - 1;
        b1 = makeMove(b1, playerMove);
        clock_t start = clock();
        if(anyMovesLeft(&b1) && evaluate(&b1) != -10000)
        {
            eval = alphabeta_basic(&b1, DEPTH, -10000, 10000);
            printf("\nEvaluate: %d\n\n", eval);
        }
        else
        {
            displayboard(&b1);
            break;
        }
        displayboard(&b1);
        clock_t stop = clock();
        int t = (stop - start)/1000000;
        printf("Time: %d\n", t);
    }

    //bot vs bot
    /*while(anyMovesLeft(&b1) && evaluate(&b1) != 10000)
    {
        int eval;
        
        clock_t start1 = clock();
        if(anyMovesLeft(&b1) && evaluate(&b1) != 10000)
        {
            eval = alphabeta_basic(&b1, DEPTH, -10000, 10000);
            printf("\nEvaluate: %d\n\n", eval);
        }
        else
        {
            displayboard(&b1);
            break;
        }
        displayboard(&b1);
        clock_t stop1 = clock();
        int t1 = (stop1 - start1)/1000000;
        printf("Time: %d\n", t1);

        clock_t start = clock();
        if(anyMovesLeft(&b1) && evaluate(&b1) != -10000)
        {
            eval = alphabeta_basic(&b1, DEPTH, -10000, 10000);
            printf("\nEvaluate: %d\n\n", eval);
        }
        else
        {
            displayboard(&b1);
            break;
        }
        displayboard(&b1);
        clock_t stop = clock();
        int t = (stop - start)/1000000;
        printf("Time: %d\n", t);
    }/*

    if(evaluate(&b1) == 10000)   printf("You lost!\n\n");
    else if(evaluate(&b1) == -10000)  printf("You won!\n\n");
}*/
