by felipetdsa
email: felipetdsa@gmail.com

# Bitcoin---Is-wallet-used-
Verify wallets from a text file if any wallet was used yet.

Use this to check if any wallet was already used in blockchain
Return Wallets already used.
Use a list generated with vanitygen

generate a wallet list using:
./vanitygen -k 1 > wallet_list_name.txt

Usage in Python:
is_used(Wallet_list) or is_used(loadWord('wallet_list_name.txt))
