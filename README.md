# Hide & Seek

**Hide & Seek** es un juego interactivo desarrollado en Python que simula el clásico juego de escondite. Este proyecto combina programación orientada a objetos, gráficos 2D e inteligencia artificial para ofrecer una experiencia divertida y desafiante.

---

## **Simulación del Juego:**

Crear un entorno virtual donde los jugadores puedan esconderse y buscarse.
Asignación aleatoria de roles (escondedor o buscador).

---

## **Características del Proyecto**

- **Juego Interactivo:**
    - Asignación aleatoria de roles: "Escondedor" o "Buscador".
    - Escenarios dinámicos con múltiples áreas para esconderse y explorar.
    - Sistema de turnos para encontrar a los escondidos.

- **Inteligencia Artificial:**
    - Un buscador controlado por IA que analiza y explora las zonas más probables de escondite.
    - Algoritmos básicos para encontrar a los escondidos en tiempo real.

- **Puntajes y Reglas:**
    - Sistema de puntos basado en el tiempo que los escondidos permanecen ocultos.
    - Penalizaciones si el buscador no encuentra a todos dentro del límite de tiempo.

- **Gráficos y Entorno:**
    - Entorno 2D desarrollado con **Pygame**.
    - Recursos visuales (imágenes y sonidos) incluidos para mejorar la experiencia.

- **Librerías Recomendadas:**
    - Random: Para asignaciones aleatorias de roles y posiciones.
    - NumPy o Matplotlib: Para análisis o visualización de estrategias de la IA.

---

## **Pasos Iniciales**

- **Diseñar un Esquema del Juego:**
    - Dibujar un diagrama de flujo para las reglas del juego.
    - Especificar cómo serán detectados.

- **Pruebas y Mejoras:**

    - Realizar pruebas unitarias para asegurarse de que las reglas y funciones se implementan correctamente.
    - Ajustar la dificultad del juego y los parámetros del entorno.

---

## **Mapa del Juego**

El mapa representa una casa con las siguientes localizaciones:

### **Segundo Piso**
1. En el armario de la habitación auxiliar delantera del segundo piso.
2. Debajo de la cama de la habitación auxiliar delantera del segundo piso.
3. En el armario de la habitación auxiliar trasera del segundo piso.
4. Debajo de la cama de la habitación auxiliar trasera del segundo piso.
5. En el armario de la habitación principal del segundo piso.
6. Debajo de la cama de la habitación principal del segundo piso.
7. En el baño del segundo piso.
8. En la ducha del baño del segundo piso.

### **Primer Piso**
9. En el baño del primer piso.
10. En el armario del baño del primer piso.
11. En el armario del patio en el primer piso.
12. En el armario del estudio del primer piso.
13. Debajo del escritorio del estudio del primer piso.
14. Debajo de la mesa del comedor del primer piso.
15. Detrás de la nevera en la cocina del primer piso.
16. En el auto en el garaje del primer piso.

---

## **Créditos**
    - Desarrollador: Ivan Moreno
    - Fecha de inicio: Diciembre de 2024
    - Inspiración: Juego clásico de escondite