import secrets
import string
import sys


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True,
) -> str:
    """Gera uma palavra-passe segura e pseudoaleatória usando o módulo secrets.

    Args:
        length (int): Comprimento da palavra-passe (mínimo 8).
        use_uppercase (bool): Incluir letras maiúsculas.
        use_digits (bool): Incluir números.
        use_special (bool): Incluir caracteres especiais.

    Returns:
        str: A palavra-passe gerada.
    """
    if length < 8:
        raise ValueError("O comprimento mínimo da palavra-passe deve ser 8.")

    # Caracteres base (Garante pelo menos minúsculas)
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_characters = lowercase + uppercase + digits + special

    if not all_characters:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")

    # Garantir que a palavra-passe contém pelo menos um caractere de cada tipo selecionado
    password = []
    if use_uppercase:
        password.append(secrets.choice(uppercase))
    if use_digits:
        password.append(secrets.choice(digits))
    if use_special:
        password.append(secrets.choice(special))
    password.append(secrets.choice(lowercase))

    # Preencher o resto do comprimento da palavra-passe
    password.extend(
        secrets.choice(all_characters) for _ in range(length - len(password))
    )

    # Baralhar a lista de forma segura e converter para string
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main():
    print("=== Gerador de Palavras-Passe Seguras ===")
    try:
        length = int(
            input("Introduza o comprimento da palavra-passe (Mínimo 8) [16]: ")
            or 16
        )
        pwd = generate_password(length=length)
        print(f"\n[+] Palavra-passe gerada com sucesso: {pwd}\n")
    except ValueError as e:
        print(f"[-] Erro de validação: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        print("\n[-] Operação cancelada pelo utilizador.")
    finally:
        # Mantém a janela aberta até pressionar Enter
        input("\nPressione Enter para sair...")


if __name__ == "__main__":
    main()
