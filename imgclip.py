import matplotlib.pyplot as plt
import matplotlib.patches as patches

name = input("image file relative dir/name: ")
image = plt.imread(name)

# since image is an array with rgb values ... to see this print(image)
# print(image, "\n---\n")
# we can use array slicing to ignore the rgb values
# image = image[:, :, 0] just 1st entries 
# image = image[:, :, 1] just 2nd entries
# image = image[:, :, 2] just 3rd entries
# print(image, "\n---\n")


fig, ax = plt.subplots()
im = ax.imshow(image)
# alternatively, we can use im = ax.imshow(image, cmap='gray') after using array slicing above
# plt.colorbar(im)

patch = patches.Circle((700, 300), radius=350, transform=ax.transData)
im.set_clip_path(patch)

ax.axis('off')

# need to have this before plt.show() 
new_img = input("save img relative dir/name: ")
fig.savefig(new_img)

plt.show()



