import cv2
import mediapipe as mp

def get_coordinates(nom):
    chosen_index = [6, 10, 14, 18]
    chosen_coordinates = []
    # Initialiser la capture vidéo avec le fichier vidéo.
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' ')) # Définir le codec pour la caméra thermique, Y16 est un format de pixel 16 bits
    cap.set(cv2.CAP_PROP_CONVERT_RGB, 0) # Désactiver la conversion en RGB

    # Configurer MediaPipe Hands pour le suivi des mains.
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.1, min_tracking_confidence=0.1)

    # Commencer une boucle pour traiter chaque frame de la vidéo.
    while True:
        # Lire une frame à partir de l'objet de capture vidéo.
        success, img = cap.read()
        if not success:
            break

        # Convertir l'image en niveaux de gris en image RGB.
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgRGB = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

        # Traiter l'image RGB pour trouver les repères des mains.
        results = hands.process(imgRGB)

        # Obtenir les repères des mains s'ils sont détectés.
        multiLandMarks = results.multi_hand_landmarks

        print(multiLandMarks)

        # Si des repères de mains sont détectés, itérer à travers eux puis quitter la boucle.
        if multiLandMarks is not None and len(multiLandMarks) == 2:
            # Itérer à travers chaque ensemble de repères de mains.
            for i, handLms in enumerate(multiLandMarks):
                # Dessiner les repères des mains et les connexions sur la frame originale.

                # Itérer à travers chaque repère pour obtenir son index et ses coordonnées.
                for idx, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape  # Obtenir les dimensions de l'image.
                    cx, cy = int(lm.x * w), int(lm.y * h)  # Calculer les coordonnées en pixels.
                    if idx in chosen_index:
                        chosen_coordinates.append([cx,cy])
                        list_of_temp = get_temperature(img, chosen_coordinates)

                # Sauvegarder les températures correspondant aux points sélectionnés.
                with open("coordinates.txt", "w") as f:
                    for i in range(len(chosen_coordinates)):
                        f.write(f"{chosen_coordinates[i][0]} {chosen_coordinates[i][1]} {list_of_temp[i]}\n")
            
            break

        # Quitter la boucle si la touche échappement est pressée.
        if cv2.waitKey(1) == 27:
            break

    # Dessiner les points sur l'image.
    for x, y in chosen_coordinates:
        cv2.circle(img, (x, y), 2, (255, 0, 0), -1)

    # Sauvegarder l'image avec les points dessinés dessus.
    cv2.imwrite(f"{nom}/coordinates.jpg", img)
    
    # Libérer l'objet de capture vidéo et fermer toutes les fenêtres lorsqu'on a terminé.
    cap.release()
    cv2.destroyAllWindows()

def get_temperature(frame_thermal, coordonnee_choisi):
    TEMPERATURE_MIN = 20 # Température minimale de la caméra en °C
    TEMPERATURE_MAX = 36 # Température maximale de la caméra en °C
    list_of_temp = [] # Liste pour stocker les températures
    for coord in coordonnee_choisi: # Boucler à travers la liste des points où l'utilisateur a cliqué
        x_mouse, y_mouse = coord
        value_pointer = frame_thermal[y_mouse, x_mouse][0] # Obtenir la valeur du pixel à la position du clic de la souris (indice 0 car l'image est en niveaux de gris)
        temperature_pointer = (value_pointer / 255.) * (TEMPERATURE_MAX - TEMPERATURE_MIN) + TEMPERATURE_MIN # Normaliser la température à la plage de la caméra
        list_of_temp.append(temperature_pointer) # Ajouter la température à la liste des températures

    return list_of_temp
