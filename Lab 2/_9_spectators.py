def get_nu_pot_viziona (spectator_list) :

    nu_pot_viziona = []

    for column in range( 0, len(spectator_list[0]) ) :
        
        inalt = 0

        for row in range( 0, len(spectator_list) ) :
            
            if (spectator_list[row][column] > inalt) :
                inalt = spectator_list[row][column]
            else :
                spectator_mic_coord = (row, column)
                nu_pot_viziona.append(spectator_mic_coord)

    return nu_pot_viziona


spectatori = [[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 7, 5]] 

print(get_nu_pot_viziona(spectatori))