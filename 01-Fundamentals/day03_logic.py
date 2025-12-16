# Day 3: Logic & Control Flow
# Goal: Use if/else statements to make decisions based on data.

# Scenario: A simple bot checking gas fees for a crypto transaction.

wallet_balance = 100.00
gas_fee = 15.50
kyc_verified = True  # Boolean (True/False switch)

print("--- Transaction Start ---")

# 1. The Decision Gate
# 'if' checks if the math is true.
if wallet_balance >= gas_fee:
    print("✅ Solvency Check: PASS")
    
    # 2. Nested Logic (Decision inside a decision)
    if kyc_verified:
        print("🚀 Process: Transferring funds...")
        new_balance = wallet_balance - gas_fee
        print(f"Transaction Complete. New Balance: ${new_balance}")
    else:
        print("⛔ Error: User Identity Verification Failed.")

else:
    # This runs ONLY if the first check (wallet_balance) failed
    print("❌ Error: Insufficient funds for gas fee.")
    print(f"Shortfall: ${gas_fee - wallet_balance}")
