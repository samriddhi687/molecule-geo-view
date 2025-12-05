import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_xyz(filename):
    #Read an XYZ file and return atoms+coordinates
    atoms=[]
    coords=[]
    with open(filename,"r") as f:
        lines=f.readlines()
    for line in lines[2:]:     #Skip first 2 lines (atom count+comment)
        parts=line.split()
        if len(parts)>=4:
            atoms.append(parts[0])
            coords.append([float(parts[1]),float(parts[2]),float(parts[3])])
    return atoms,coords

def visualize_molecule(atoms,coords):
    #Plot molecule in 
    fig=plt.figure()
    ax=fig.add_subplot(111,projection="3d")
    xs=[c[0] for c in coords]
    ys=[c[1] for c in coords]
    zs=[c[2] for c in coords]
    #Draw atoms
    ax.scatter(xs,ys,zs,s=200,depthshade=True)
    #Label atoms
    for i, atom in enumerate(atoms):
        ax.text(xs[i],ys[i],zs[i],atom,fontsize=12,weight='bold')
    ax.set_title("3D Molecular Geometry Viewer")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    plt.show()

def main():
    print("=== Molecular Geometry Viewer ===")
    filename=input("Enter XYZ file name(example:water.xyz, methane.xyz, carbondioxide.xyz, ammonia.xyz): ") #sample molecule names given in the input given
    try:
        atoms,coords=read_xyz(filename)
        visualize_molecule(atoms, coords)
    except FileNotFoundError:
        print("File not found. Make sure it is in the same folder as this script.")
    except Exception as e:
        print("Error:",e)
if __name__=="__main__":
    main()
