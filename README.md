### Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
### Centro de Informática (CIn) (http://www.cin.ufpe.br)
### Graduando em Sistemas de Informação
### IF969 - Algoritmos e Estrutura de Dados

### Autor: Vinícius Luiz da Silva França (vlsf2)
### Email: vlsf2@cin.ufpe.br
### Data: 2020-10-01

### Copyright(c) 2020 Vinícius Luiz da Silva França

> **GRAFO**
>
> - Grafo Matriz
>   - (não) Direcionado
>   - (não) Ponderado
>   - Prim e Kruskal
>
> - Grafo Lista de Adjacencia
>   - (não) Direcionado
>   - (não) Ponderado
>   - BFS
>   - DFS



> #### input
>
> STI, CAC, 64  
> STI, CB, 50  
> STI, CCEN, 49  
> STI, CCJ, 37  
> STI, CCS, 98  
> STI, CCM, 1  
> STI, CCSA, 95  
> STI, CE, 89  
> STI, CFCH, 80  
> STI, CIn, 71  
> STI, CTG, 52  
> CAC, STI, 3  
> CAC, CB, 45  
> CAC, CCEN, 56  
> CAC, CCJ, 20  
> CAC, CCS, 36  
> CAC, CCM, 7  
> CAC, CCSA, 14  
> CAC, CE, 70  
> CAC, CFCH, 97  
> CAC, CIn, 27  
> CAC, CTG, 43  
> CB, STI, 99  
> CB, CAC, 26  
> CB, CCEN, 44  
> CB, CCJ, 43  
> CB, CCS, 50  
> CB, CCM, 10  
> CB, CCSA, 50  
> CB, CE, 42  
> CB, CFCH, 36  
> CB, CIn, 99  
> CB, CTG, 16  
> CCEN, STI, 49  
> CCEN, CAC, 8  
> CCEN, CB, 27  
> CCEN, CCJ, 76  
> CCEN, CCS, 3  
> CCEN, CCM, 56  
> CCEN, CCSA, 93  
> CCEN, CE, 67  
> CCEN, CFCH, 3  
> CCEN, CIn, 13  
> CCEN, CTG, 22  
> CCJ, STI, 96  
> CCJ, CAC, 79  
> CCJ, CB, 77  
> CCJ, CCEN, 79  
> CCJ, CCS, 56  
> CCJ, CCM, 97  
> CCJ, CCSA, 24  
> CCJ, CE, 44  
> CCJ, CFCH, 38  
> CCJ, CIn, 16  
> CCJ, CTG, 8  
> CCS, STI, 73  
> CCS, CAC, 69  
> CCS, CB, 62  
> CCS, CCEN, 35  
> CCS, CCJ, 90  
> CCS, CCM, 83  
> CCS, CCSA, 64  
> CCS, CE, 46  
> CCS, CFCH, 54  
> CCS, CIn, 7  
> CCS, CTG, 27  
> CCM, STI, 96  
> CCM, CAC, 84  
> CCM, CB, 72  
> CCM, CCEN, 48  
> CCM, CCJ, 73  
> CCM, CCS, 19  
> CCM, CCSA, 92  
> CCM, CE, 23  
> CCM, CFCH, 26  
> CCM, CIn, 46  
> CCM, CTG, 58  
> CCSA, STI, 89  
> CCSA, CAC, 86  
> CCSA, CB, 7  
> CCSA, CCEN, 5  
> CCSA, CCJ, 41  
> CCSA, CCS, 40  
> CCSA, CCM, 97  
> CCSA, CE, 48  
> CCSA, CFCH, 29  
> CCSA, CIn, 19  
> CCSA, CTG, 72  
> CE, STI, 60  
> CE, CAC, 9  
> CE, CB, 13  
> CE, CCEN, 17  
> CE, CCJ, 7  
> CE, CCS, 12  
> CE, CCM, 22  
> CE, CCSA, 18  
> CE, CFCH, 94  
> CE, CIn, 76  
> CE, CTG, 84  
> CFCH, STI, 52  
> CFCH, CAC, 25  
> CFCH, CB, 35  
> CFCH, CCEN, 92  
> CFCH, CCJ, 27  
> CFCH, CCS, 77  
> CFCH, CCM, 40  
> CFCH, CCSA, 64  
> CFCH, CE, 91  
> CFCH, CIn, 19  
> CFCH, CTG, 3  
> CIn, STI, 88  
> CIn, CAC, 4  
> CIn, CB, 67  
> CIn, CCEN, 32  
> CIn, CCJ, 92  
> CIn, CCS, 4  
> CIn, CCM, 15  
> CIn, CCSA, 18  
> CIn, CE, 18  
> CIn, CFCH, 31  
> CIn, CTG, 18  
> CTG, STI, 20  
> CTG, CAC, 94  
> CTG, CB, 5  
> CTG, CCEN, 29  
> CTG, CCJ, 55  
> CTG, CCS, 84  
> CTG, CCM, 66  
> CTG, CCSA, 10  
> CTG, CE, 48  
> CTG, CFCH, 60  
> CTG, CIn, 4  

  