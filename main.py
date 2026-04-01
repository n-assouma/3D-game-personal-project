from game import Game 

if __name__ == '__main__':
    my_game = Game()
    try:
        my_game.run()
    except KeyboardInterrupt:
        my_game.exit()

    