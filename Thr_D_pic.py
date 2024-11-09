import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol
def Three_D(name):
    compounds = pcp.get_compounds(f'{name}', 'name')
    if compounds:
        molecule = compounds[0]
        # 获取分子的SMILES字符串
        smiles = molecule.isomeric_smiles
        print(f"SMILES: {smiles}")

        # 使用 RDKit 创建分子对象
        mol = Chem.MolFromSmiles(smiles)

        # 生成3D坐标
        mol = Chem.AddHs(mol)  # 添加氢原子
        AllChem.EmbedMolecule(mol, randomSeed=42)

        # 创建一个3D可视化对象
        viewer = py3Dmol.view(width=800, height=600)
    
        # 将RDKit分子转换为3D坐标并加载到可视化工具
        block = Chem.MolToMolBlock(mol)
        viewer.addModel(block, "mol")

        # 渲染并显示3D分子结构
        viewer.setStyle({'stick': {}})
        viewer.zoomTo()
        viewer.show()
    else:
        print("未能找到分子")
Three_D("Malonic acid")
