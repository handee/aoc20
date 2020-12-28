subject=7
divisor=20201227
public_key_m=6929599
public_key_d=2448427
public_key_d_t=17807724
public_key_m_t=5764801

def iterate(v,s):
    v=v*s
    v=v%divisor
    return(v)

def part_one():
    door_loop=1
    my_loop=1
    door_key=1
    my_key=1
    while door_key != public_key_d :
        door_key=iterate(door_key,subject)
        print(f"iteration {door_loop}: door_key={door_key} aiming for={public_key_d}")
        door_loop+=1

    while my_key != public_key_m:
        my_key=iterate(my_key,subject)
        print(f"iteration {my_loop}: my_key={my_key} aiming for={public_key_m}")
        my_loop+=1
    encryption_key=1
    for i in range(my_loop):
        print(f"iteration {i}: encryption_key={encryption_key}")
        encryption_key=iterate(encryption_key,public_key_d)


part_one()
        
