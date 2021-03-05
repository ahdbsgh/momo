import torch
seed = 32

x = torch.ones(2, 2, requires_grad=True)
y = x + 2
z = y * y * 3
out = z.mean()

a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
# print(a)
# print(a.requires_grad)
# a.requires_grad_(True)
# print(a.requires_grad)
# b = (a * a).sum()
# print(b.grad_fn)

out.backward()
print(x.grad)