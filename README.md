# sliding_puzzle
Representation of an N*M sliding puzzle as well as a number of implemented ways to solver, from searching algorithms, trees, planning, and estochastic methods.

## Problem
Given an n*m matrix of the following form:

\begin{equation}
\begin{bmatrix} 
c_{1,1} & c_{1,2} & c_{1,3} & ... & c_{1,m} \\
c_{2,1} & ... &....& ...& c_{2,m}\\
...& ...& ...& ...& ...\\
c_{n,1} & c_{n,2} & c_{n,3} & ...& c_{n,m} 
\end{bmatrix}
\end{equation}

Where:

$$
c_{n,m} =0
$$

And any other element C_(i,j) tienen valores numéricos no repetidos que van de 1 a (n*m)-1, asignados aleatoriamente.

Se quiere ordenar los elementos de la matriz de tal forma que C_(1,1) = 1, C_(1,2) = 2, …, C_(1,m) = m y C_(2,1) = m+1, C_(2,2) = m+2, … C_(n,1) = (n-1)*m + 1, C_(n,m-1) = (n*m)-1 y C_(n,m) = 0.

Para esto, se puede mover el 0 que inicialmente se encuentra en la posición C_(n,m) de la siguiente manera:

- El 0 puede moverse una casilla hacia arriba, hacia abajo, hacia la derecha o hacia la izquierda, mientras no se salga de los límites de la matriz, la casilla actual del 0 pasará a estar ocupada por el elemento que originalmente estaba en la casilla hacia donde el 0 se movió.
- No son válidos movimientos en diagonal.




## Representation
Representación:

Asignar un indice fijo a cada casilla, este indice no se mueve, representa una posición o coordenada en la matriz:

$$
\begin{bmatrix} 
c_0 & c_1 & c_2 & c_3 & c_4 \\\\
c_5 & c_6 & c_7 & c_8 & c_9 \\\\
c_{10} & c_{11} & c_{12} & c_{13} & c_{14}\\\\
c_{15} & c_{16} & c_{17} & c_{18} & c_{19}\\\\
c_{20} & c_{21}& c_{22} & c_{23} & c_{24} 
\end{bmatrix}
$$

$$
\begin{bmatrix} 
c_0 & c_1 & c_2 & ... & c_{m-1} \\\\
c_{m} & c_{m+1} &....& ...& c_{2m-1}\\\\
c_{2m}& c_{2m+1}& c_{2m+2} & ...& c_{3m-1}\\\\
... & ... & ... &... &... \\\\
c_{(n-1)*m} & c_{(n-1)*m+1} & c_{(n-1)*m+2} & ...& c_{(n*m)-1} 
\end{bmatrix}
$$

El indice representa la casilla. Es un indice fijo.

$$
X=s=\begin{bmatrix} 
c_0 & c_1 & c_2 & c_3 & ... & c_{(n*m)-1}
\end{bmatrix}
$$

$$
c_i \in \{1 , 2, 3, ... ,(n*m)-1\}
$$

$$
\forall c_i \forall c_j \{c_i\ = c_j \leftrightarrow i=j\}
$$

$$
s_0 = \begin{bmatrix} 
c_0 & c_1 & c_2 & c_3 & ... & c_{(n*m)-1}
\end{bmatrix}
$$

$$
c_i \sim \{1 , 2, 3, ... (n*m)-1\}
$$

$$
\forall c_i \forall c_j \{c_i\ = c_j \leftrightarrow i=j\}
$$

$$
c_{(n*m)-1} =0
$$

$$
goal = s = \begin{bmatrix} 
c_0 & c_1 & c_2 & c_3 & ... & c_{(n*m)-1}
\end{bmatrix}
$$

$$
\{c_1,c_2,...c_{(n*m)-1}\} = \{1 , 2, 3, ... ,(n*m)-1, 0\}
$$

$$
T(s) = [i,d](s) = \begin{cases}
c_i = c_i & c_i \ne 0 \\
(c_i = c_{i+d} , c_{i+d} = 0) & c_i = 0 \\
\end{cases}
$$

$$
0 \le i+d \le (n*m)-1 \; , \; d \in \{m,-m,1,-1\}
$$
