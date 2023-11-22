input_price = 5
output_price = 10 

input_balance= 9 
output_balance=  10

input_required_ratio = 0.2
output_required_ratio = 0.4 

required_ratio = input_required_ratio / output_required_ratio
print("required_ratio :", required_ratio)

input_vault_value = input_balance * input_price
output_vault_value = output_balance * output_price
print("input_vault_value :", input_vault_value)
print("output_vault_value :", output_vault_value)

current_ratio = input_vault_value / output_vault_value
print("current_ratio : ", current_ratio)

ratio_gap = ((1 - (current_ratio / required_ratio)) / 2)
print("ratio_gap : ", ratio_gap)

value_gap = output_vault_value * ratio_gap
print("value_gap :", output_price)

token_gap = value_gap / output_price
print("token_gap : ", token_gap)

amount = token_gap 
io_ratio = input_price / output_price 
print("amount : ", amount)
print("io_ratio:", io_ratio)

new_input_balance = input_balance + (amount * io_ratio)
new_output_balance = output_balance - amount
print("new_input_balance :", new_input_balance)
print("new_output_balance :", new_output_balance)

new_input_value = input_price * new_input_balance
new_output_value = output_price * new_output_balance
print("new_input_value :", new_input_value)
print("new_output_value :", new_output_value)

new_ratio = new_input_value / new_output_value
print("required_ratio :", required_ratio)
print("new_ratio", new_ratio)

