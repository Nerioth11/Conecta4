# Conecta4
TicTacToe application coded in Python which you can play against or use 2 machines to play against each other.

Este trabajo consiste en una implementación del juego "Conecta 4", programado para realizar, tanto partidas entre la IA 
(utilizando heurísticas propias) y un humano, como para realizar partidas entre nuestra IA y heurísticas realizadas por otros compañeros.

Se han modificado los siguientes archivos:
# run.py

  - ```obtenerTipoPartida()``` permite escoger partida máquina vs máquina o humano vs máquina
  - ```obtenerHeurísticaMáquina()``` permite escoger uno de los tres niveles de dificultad (0 random, 1 medio, 
2 difícil)
  - ```obtenerJugadorQueEmpieza()``` permite escoger qué jugador mueve en el primer turno, X o O. En el bucle while,
añadimos una comprobación para comprobar si nos encontramos en un estado final, si es así, comprobamos si la
partida ha terminado en empate o cuál de los jugadores ha ganado.

# utils.py

- ```argmin``` añadimos un print que muestra el movimiento, el valor de la heurística 
y el state.utility.

- En la clase Struct definimos una función de hash que utilizaremos para el patrón memoize.

# games.py

- En la clase TicTacToe modificamos la función display para ofrecer una mejor visualización de la 
partida, mostrando colores distintos para cada casilla según si la ficha es O, X o si es un espacio vacío.

# heuristicas.py

- ```memoize(f)``` define el patrón memoize para reducir los tiempos de espera en nuestra heurística, 
reciclando los estados que han sido previamente calculados.

- ```check_legal_position(x,y)``` comprueba que la posición (x,y) se encuentra entre los límites del tablero.

- ```count_empty_holes(board, x, y)``` comprueba cuántos huecos vacíos hay por debajo de una posición dada.

- ```heuristicaBuena(state)``` usa el patrón memoize. Se encarga de calcular, estudiando previamente si la partida
ha sido ganada o perdida (comprobando state.utility), un valor de  heurística usando la función k_in_row_bueno(),
evaluando, para cada movimiento legal, la posibilidad de lograr un k_in_row que tiene cada jugador.

- ```k_in_row_bueno(board, move, player, rival, (delta_x, delta_y))``` hemos reutilizado el k_in_row que se nos ha proporcionado
y lo hemos adaptado para que devuelva un valor de heurística, evaluando si el jugador pasado tiene, desde esa posición,
la posibilidad de conseguir un 4 en raya o no.

 - Si tenemos una pieza ocupada por el jugador actual, sumamos 10 + 10*k (para premiar que haya 
varias posiciones contiguas que no están ocupadas por el rival).

 - Si tenemos un hueco vacío, restamos count_empty_holes() / k (para penalizar menos en el 
caso de que se hayan encontrado varias posiciones contiguas no ocupadas por el rival).

 - Si se ha detectado que desde esa posición hay un k_in_row posible, se devuelve el valor 
de la heurística, en caso contrario, se devuelve un valor negativo bastante grande.
	
- ```heurisiticaRegular(state)``` también utiliza el patrón memoize. Tiene el mismo funcionamiento que heurísticaBuena,
pero no evalua los movimientos legales del rival.

- ```k_in_row_regular(board, move, rival, (delta_x, delta_y))``` sigue un procedimiento similar que  k_in_row_bueno,
salvo que no se penalizan los huecos vacíos. 

 - Si la posición contiene una ficha del jugador, sumamos 10.

 - Si la posición está vacía sumamos 5, simplificando el cálculo de la heurística.

 - Si se ha detectado que desde la posición pasada hay un k_in_row posible, se devuelve el valor 
de la heurística, en caso contrario se devuelve 0.

