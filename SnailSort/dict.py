d = {}
for _ in range(int(input())):
    name, product, quantity = input().split()
    d[name] = d.setdefault(name, dict())
    d[name][product] = d[name].get(product, 0) + int(quantity)

for names, products in sorted(d.items()):
    print(f"{names}:")
    for quantities in sorted(products):
        print(f"{quantities} {products[quantities]}")