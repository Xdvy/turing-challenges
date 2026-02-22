def multiples_five_and_seven(max_value):
    return (i for i in range(max_value) if i % 5 == 0 or i % 7 == 0)

def compute_sum_multiples(max_value):
    return sum(multiples_five_and_seven(max_value))

class Challenge001:
    """
    Trouver la somme de tous les multiples de 5 ou de 7.
    """

    def solve(self, max_value: int) -> int:
        return compute_sum_multiples(max_value)

