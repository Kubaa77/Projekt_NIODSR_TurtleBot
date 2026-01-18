# Interfejs Sterowania Robotem TurtleBot3

System umożliwia sterowanie mobilnym robotem TurtleBot3 (model Burger) za pomocą prostego interfejsu graficznego.

## Funkcjonalność
* ✅ **Węzeł sterujący:** Węzeł sterujący napisany w Pythonie (`rclpy`, `OpenCV`), publikujący na topic `/cmd_vel`.
* ✅ **Logika sterowania:**
    * Kliknięcie w górną połowę okna -> Jazda do przodu.
    * Kliknięcie w dolną połowę okna -> Jazda do tyłu.
* ✅ **Plik launch** `sterowanie.launch.py` automatycznie uruchamia symulację Gazebo (TurtleBot3 Burger) oraz sterownik robota.
* ✅ **Dockeryzacja:** Przygotowany `Dockerfile` oraz skrypt `run_docker.sh` dla środowiska plug-and-play.

## Struktura projektu
* `src/sterowanie_robotem/` - Kod źródłowy paczki (node sterujący).
* `launch/` - Zawiera plik `sterowanie.launch.py`.
* `Dockerfile` - Konfiguracja kontenera Docker.
* `run_docker.sh` - Skrypt do automatycznego budowania i uruchamiania projektu.


## Instrukcja uruchomienia

### Opcja A: Docker (Plug-and-Play)
Ta metoda nie wymaga posiadania zainstalowanego ROS 2 na komputerze. Wymagany jest jedynie zainstalowany silnik Docker.

Aby uruchomić projekt, najpierw pobierz repozytorium na swój komputer i wejdź do katalogu projektu:
```bash
git clone https://github.com/Kubaa77/Projekt_NIODSR_TurtleBot.git
cd Projekt_NIODSR_TurtleBotO
```

Skrypt `run_docker.sh` automatycznie:
1. Buduje obraz z niezbędnymi zależnościami (ROS 2, OpenCV).
2. Konfiguruje przekazywanie obrazu graficznego (GUI).
3. Uruchamia symulację i sterownik.

**Komendy:**
```bash
# 1. Nadaj uprawnienia wykonywania (tylko pierwszy raz)
chmod +x run_docker.sh

# 2. Uruchom projekt
./run_docker.sh
```

### Opcja B:Uruchomienie Lokalne 

Ta metoda wymaga lokalnie zainstalowanego ROS 2 Humble oraz pakietów symulacyjnych TurtleBot3.

Proces uruchomienia obejmuje:
1. Zbudowanie paczki `sterowanie_robotem` w lokalnym workspace.
2. Załadowanie środowiska ROS 2.
3. Konfigurację modelu robota TurtleBot3.
4. Uruchomienie symulacji oraz węzłów sterowania.

**Komendy:**
```bash
# Przejście do katalogu workspace
cd ~/ros2_ws

# Budowanie paczki
colcon build --packages-select sterowanie_robotem

# Załadowanie środowiska ROS 2
source install/setup.bash

# Ustawienie modelu TurtleBot3
export TURTLEBOT3_MODEL=burger

# Uruchomienie systemu
ros2 launch sterowanie_robotem sterowanie.launch.py