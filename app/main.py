from atm_controller import AtmController


def main():
    atm_controller = AtmController()
    atm_controller.run()    


# NOTE: If executed from terminal, calls main function (won't be called if we import function into another module)
if __name__ == '__main__':
    main()