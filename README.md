

Este proyecto consiste en una implementacion del juego clasico del ahorcado utilizando el lenguaje de programacion Python. El objetivo es adivinar una palabra secreta seleccionada de forma aleatoria, letra por letra, antes de agotar el numero de intentos permitidos.


El programa ha sido desarrollado utilizando estructuras fundamentales de Python para garantizar un codigo legible y eficiente:

1. Importacion de Modulos: Se utiliza el modulo random para la seleccion aleatoria de elementos dentro de una lista.
2. Estructuras de Datos: Se emplean listas para almacenar tanto el diccionario de palabras posibles como el estado actual de la palabra que el usuario intenta adivinar.
3. Bucles de Control: 
   - Se utiliza un bucle while para mantener el ciclo del juego activo mientras el usuario tenga intentos disponibles y falten letras por descubrir.
   - Se emplea un bucle for para recorrer la palabra secreta y actualizar las posiciones acertadas.
4. Logica Condicional: Se aplican sentencias if, elif y else para validar si la entrada del usuario es una letra valida, si ya ha sido ingresada previamente o si coincide con algun caracter de la palabra objetivo.
5. Manipulacion de Strings: Se utilizan metodos como .lower() para estandarizar la entrada de datos y .join() para presentar el progreso del juego de manera clara en la consola.

Para ejecutar este programa, asegurese de tener instalado Python 3 en su equipo.

1. Descargue el archivo ahorcado.py en su directorio local.
2. Abra una terminal o linea de comandos.
3. Dirijase a la carpeta donde se encuentra el archivo.
4. Ejecute el comando:
   python ahorcado.py

1. Al iniciar, el programa seleccionara una palabra al azar y mostrara una serie de guiones que representan la longitud de la misma.
2. El jugador dispone de un maximo de 6 intentos fallidos.
3. En cada turno, el jugador debe ingresar una sola letra.
4. Si la letra es correcta, se revelara su posicion en la palabra.
5. Si la letra es incorrecta, se restara un intento al contador.
6. El juego termina cuando el jugador adivina la palabra completa o cuando los intentos se agotan.
