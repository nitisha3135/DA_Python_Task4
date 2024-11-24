def user_account(username, password, email):
    print(f'username = {username}')
    print(f'password = {password}')
    print(f'email = {email}')
    
    return {
        'user-name': username,
        'user-password':password,
        'user-email':email
    }

print()
user1=user_account('Spongebob','abc123','spongebob@gmail.com')
print(f'user1 = {user1}')
print()
user2=user_account('Patrick','xyz456','patrick@gail.com')
print(f'user2 ={user2}')
print()
user3=user_account('Kevin','pqr789','kevin@gmail.com')
print(f'user3 = {user3}')
print()




def customer_feedback(customer_name, product_name, rating, review):
    print('--Customer Feedback')
    print(f'customer_name = {customer_name}')
    print(f'product_name = {product_name}')
    print(f'rating = {rating}')
    print(f'review = {review}')
    
    return 'End'

print()
print(customer_feedback("Alice", "Smartphone", 4, "Great product, value for money!"))
print()
print(customer_feedback("Bob", "Laptop", 6, "Not satisfied with performance.")) 