class Solution(object):
    def strongPasswordChecker(self, password):

        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)

        missing_types = 3 - (has_lower + has_upper + has_digit)

        # Changes required to fix consecutive characters
        replacements = 0
        one_mod = 0
        two_mod = 0

        i = 2  # Start from the third character
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                if length % 3 == 0:
                    one_mod += 1
                elif length % 3 == 1:
                    two_mod += 1
                replacements += length // 3
            else:
                i += 1

        # If the password is too short
        if n < 6:
            return max(missing_types, 6 - n)

        # If the password is within the acceptable length
        elif n <= 20:
            return max(missing_types, replacements)

        # If the password is too long
        else:
            over_len = n - 20
            min_steps = over_len

            # Use over_len removals strategically to reduce the number of replacements
            # First use one_mod replacements as removing one character here reduces one replacement needed
            if over_len > 0 and one_mod > 0:
                use = min(over_len, one_mod)
                over_len -= use
                replacements -= use

            # Next use two_mod replacements as removing two characters can reduce one replacement needed
            if over_len > 0 and two_mod > 0:
                use = min(over_len, two_mod * 2) // 2
                over_len -= use * 2
                replacements -= use

            # Finally, address any remaining over_length by considering generic replacements
            if over_len > 0:
                replacements -= over_len // 3

            return min_steps + max(missing_types, replacements)
