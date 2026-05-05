nums = [1, 2, 3]  
# lista -> mutavel (da pra alterar)

print(type(nums))

nums.append(3)  
# adiciona no final

nums.append(4)
nums.append(500)

print(len(nums))  
# tamanho da lista

nums[3] = 100  
# altera valor pelo indice

nums.insert(0, -200)  
# insere na posicao 0

print(2 in nums)  
# verifica se existe na lista

print(nums[6])   # acessa posicao especifica
print(nums[-1])  # ultimo elemento
print(nums[-2])  # penultimo

print(nums)  
# lista final