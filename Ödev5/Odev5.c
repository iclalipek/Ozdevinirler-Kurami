#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX_LEN 100

// Dilin terminalleri (VT)
#define PLUS '+'
#define MINUS '-'
#define MULTIPLY '*'
#define DIVIDE '/'
#define LEFT_PARENTHESIS '('
#define RIGHT_PARENTHESIS ')'
#define VARIABLE 'v'
#define CONSTANT 'c'


bool isMathExpression(char *input);
bool parseS(char *input);
bool parseTerm(char *input);
bool parseFactor(char *input);

int main() {
    char input[MAX_LEN];
    
    while (true) {
        printf("Matematiksel ifadeyi girin (sonlandirmak icin 'q' girin): ");
        fgets(input, MAX_LEN, stdin);
        input[strcspn(input, "\n")] = '\0'; 
        
        if (strcmp(input, "q") == 0) 
            break;
        
        if (isMathExpression(input))
            printf("Girilen ifade matematiksel bir ifadedir.\n");
        else
            printf("Girilen ifade matematiksel bir ifade degildir.\n");
    }
    
    return 0;
}

bool parseS(char *input) {
    return parseTerm(input);
}

bool parseTerm(char *input) {
    if (!parseFactor(input))
        return false;
    
    while (*input == MULTIPLY || *input == DIVIDE) {
        input++; 
        if (!parseFactor(input))
            return false;
    }
    
    return true;
}

bool parseFactor(char *input) {
    if (*input == VARIABLE || *input == CONSTANT) {
        input++; // Degisken veya sabiti gec
        return true;
    } else if (*input == LEFT_PARENTHESIS) {
        input++; // '(' karakterini gec
        if (!parseS(input))
            return false;
        
        if (*input == RIGHT_PARENTHESIS) {
            input++; // ')' karakterini gec
            return true;
        } else {
            return false; // Parantezler uyumsuz
        }
    } else {
        return false; // Gecersiz karakter
    }
}

bool isMathExpression(char *input) {
    return parseS(input) && *input == '\0';
}
