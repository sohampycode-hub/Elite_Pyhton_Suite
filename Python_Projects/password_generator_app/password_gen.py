import string
import secrets

def generate_secure_password(length, include_upper, include_digits, include_special):
    """Generates a cryptographically secure password with guaranteed complexity constraints."""
    # Define baseline required character set
    lowercase_pool = string.ascii_lowercase
    uppercase_pool = string.ascii_uppercase if include_upper else ""
    digits_pool = string.digits if include_digits else ""
    special_pool = string.punctuation if include_special else ""
    
    # Combine active character pools
    combined_pool = lowercase_pool + uppercase_pool + digits_pool + special_pool
    if not combined_pool:
        return "Error: No character pools selected."
        
    if length < 4:
        return "Error: Password length must be at least 4 for complete pool distribution."

    password_chars = []
    
    # Guarantee at least one character from each selected pool is present
    password_chars.append(secrets.choice(lowercase_pool))
    if include_upper:
        password_chars.append(secrets.choice(uppercase_pool))
    if include_digits:
        password_chars.append(secrets.choice(digits_pool))
    if include_special:
        password_chars.append(secrets.choice(special_pool))
        
    # Fill the remaining length requirements from the combined pool
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(combined_pool))
        
    # Shuffle the characters using a secure method to break structural predictability
    secrets.SystemRandom().shuffle(password_chars)
    
    return "".join(password_chars)

def evaluate_strength(password, length, has_upper, has_digits, has_special):
    """Calculates a baseline password strength ranking for user feedback."""
    score = 0
    # Length evaluations
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
        
    # Pool variety evaluations
    if has_upper: score += 1
    if has_digits: score += 1
    if has_special: score += 1
    
    # Scoring matrix output mapping
    if score >= 5: return "EXCELLENT (Production-Ready / Strong Entropy)"
    if score >= 3: return "MODERATE (Acceptable for non-critical accounts)"
    return "WEAK (Vulnerable to basic computational attacks)"

def main():
    """Main CLI loop for seamless entry collection on mobile devices."""
    print("=" * 45)
    print("   CRYPTOGRAPHICALLY SECURE PASSWORD ENGINE   ")
    print("=" * 45)
    print("[INFO] Backed by the OS kernel 'secrets' module.")
    
    while True:
        try:
            print("\n--- Configuration Profile ---")
            length_input = input("Enter target password length (or 'exit'): ").strip()
            
            if length_input.lower() == 'exit':
                print("\nShutting down Security Core. Sessions terminated.")
                break
                
            length = int(length_input)
            
            # Request configuration specifications from the user
            upper = input("Include uppercase characters? (y/n): ").lower().strip() == 'y'
            digits = input("Include numerical digits? (y/n): ").lower().strip() == 'y'
            special = input("Include special punctuation symbols? (y/n): ").lower().strip() == 'y'
            
            print("\n[~] Instantiating secure entropy arrays...")
            secure_password = generate_secure_password(length, upper, digits, special)
            
            if "Error" in secure_password:
                print(f"[!] {secure_password}")
            else:
                print("\n" + "=" * 45)
                print(f"Generated Password: {secure_password}")
                print("-" * 45)
                strength = evaluate_strength(secure_password, length, upper, digits, special)
                print(f"Entropy Assessment: {strength}")
                print("=" * 45)
                
        except ValueError:
            print("\n[!] Input Error: Length variable requires a valid integer value.")

if __name__ == "__main__":
    main()
