class PasswordValidator:
    @staticmethod
    def is_valid(password):
        if len(password) < 8:
            return False

        count_digits = 0
        for c in password:
            if c.isdigit():
                count_digits += 1

        if count_digits < 1:
            return False

        return True
