class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'

    def transition(self, char):
        if self.state == 'q0':
            if char == '(':
                self.stack.append('(')
                self.state = 'q1'
            elif char.isdigit():
                self.state = 'q1'
            else:
                return False, "Geçersiz karakter başlangıcı"  # İlk karakterin sayı veya '(' olmalı
        elif self.state == 'q1':
            if char == '(':
                self.stack.append('(')
            elif char == ')':
                if not self.stack or self.stack[-1] != '(':
                    return False, "Dengeli parantez hatası"  # Dengeli parantez hatası ')' 
                self.stack.pop()
            elif char.isdigit():
                pass
            elif char in '+-*/':
                self.state = 'q2'
            else:
                return False, "Geçersiz karakter"  # Geçersiz karakter
        elif self.state == 'q2':
            if char.isdigit():
                self.state = 'q1'
            elif char == '(':
                self.stack.append('(')
                self.state = 'q1'
            else:
                return False, "Geçersiz karakter"  # Operatörden sonra sayı veya '(' olmalı
        else:
            return False, "Bilinmeyen durum"  # Bilinmeyen durum

        return True, "" 

    def is_accepted(self):
        return self.state == 'q1' and len(self.stack) == 0

    def process_input(self, input_string):
        self.stack = []
        self.state = 'q0'

        for char in input_string:
            valid, error_message = self.transition(char)
            if not valid:
                return False, error_message

        if not self.is_accepted():
            if self.state != 'q1':
                return False, "İfade tamamlanmadı"  # İfade bir sayı veya ')' ile bitmeli
            elif len(self.stack) > 0:
                return False, "Dengeli parantez hatası"  # Tüm '(' parantezleri kapanmış olmalı

        return True, "" 

def main():
    pda = PDA()
    expressions = []

    print("Matematiksel ifadeleri giriniz(Girerken arada boşluk bırakmayınız). Her ifadeden sonra Enter tuşuna basınız.")
    print("Girdi işlemi bittikten sonra 'son' yazarak işlemi sonlandırın.")

    while True:
        user_input = input()

        if user_input.lower() == 'son':
            break

        expressions.append(user_input.strip())

    print("\nİfadelerin kontrol sonuçları:")
    for expr in expressions:
        valid, error_message = pda.process_input(expr)
        if valid:
            print(f"'{expr}': Geçerli ifade!")
        else:
            print(f"'{expr}': Geçersiz ifade! [{error_message}]")

if __name__ == "__main__":
    main()
