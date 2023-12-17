from random import randint

class Password:
    """
    Created Password class for generating random passwords with specified characteristics.

    Attributes:
    None

    Methods:
    - generatePassword(length: int) -> str:
        Generates a random password with the specified length and characteristics.
        Parameters:
            - length (int): The desired length of the password.
        Returns:
            - str: The generated password.

    - shufflePassword(arr: str) -> str:
        Shuffles the characters in the provided string to add randomness.
        Parameters:
            - arr (str): The input string to be shuffled.
        Returns:
            - str: The shuffled string.

    - generateRandomNumber() -> str:
        Generates a random numeric character.
        Returns:
            - str: The generated random numeric character.

    - generateLowercase() -> str:
        Generates a random lowercase alphabetical character.
        Returns:
            - str: The generated random lowercase alphabetical character.

    - generateUppercase() -> str:
        Generates a random uppercase alphabetical character.
        Returns:
            - str: The generated random uppercase alphabetical character.

    - generateSymbol() -> str:
        Generates a random symbol from a predefined set.
        Returns:
            - str: The generated random symbol.
    """

    def generatePassword(self,length: int) -> str:
        """
        Generates a random password with the specified length and characteristics.
        
        Parameters:
            - length (int): The desired length of the password.
        
        Returns:
            - str: The generated password.
        """
        hasUpper = True
        hasLower = True
        hasNum = True
        hasSym = True
        password = ""
        funArr = []

        # Add functions to the array based on specified characteristics
        if hasUpper:
            funArr.append(self.generateUppercase)
        if hasLower:
            funArr.append(self.generateLowercase)
        if hasNum:
            funArr.append(self.generateRandomNumber)
        if hasSym:
            funArr.append(self.generateSymbol)

        # Generate password using selected functions
        for i in range(len(funArr)):
            password += funArr[i]()
        
        # Fill remaining length with characters from randomly selected functions
        for i in range(length - len(funArr)):
            rndIndex = randint(0, len(funArr) - 1)
            password += funArr[rndIndex]()

        return self.shufflePassword(password)

    def shufflePassword(self,arr: str) -> str:
        """
        Shuffles the characters in the provided string to add randomness.
        It uses fisher yates algorithm.
        
        Parameters:
            - arr (str): The input string to be shuffled.
        
        Returns:
            - str: The shuffled string.
        """
        arr = arr.split()
        n = len(arr)
        for i in range(n - 2, 0, -1):
            j = randint(0, i + 1)
            arr[i], arr[j] = arr[j], arr[i]
        password = ""
        for i in arr:
            password += i
        return password

    def generateRandomNumber(self) -> str:
        """
        Generates a random numeric character.
        
        Returns:
            - str: The generated random numeric character.
        """
        return str(randint(0, 9))

    def generateLowercase(self) -> str:
        """
        Generates a random lowercase alphabetical character.
        
        Returns:
            - str: The generated random lowercase alphabetical character.
        """
        return chr(randint(97, 123))

    def generateUppercase(self) -> str:
        """
        Generates a random uppercase alphabetical character.
        
        Returns:
            - str: The generated random uppercase alphabetical character.
        """
        return chr(randint(65, 91))

    def generateSymbol(self) -> str:
        """
        Generates a random symbol from a predefined set.
        
        Returns:
            - str: The generated random symbol.
        """
        symbol = '~`!@#$%^&*()_-+={[}]|:;"<,>.?/'
        rndInt = randint(0, len(symbol) - 1)
        return symbol[rndInt]
