
# Blender 3.x+ — Mars system animado
import bpy, math
def clear_scene():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
def create_uv_sphere(name, r, seg=48, rings=24, color=(0.76,0.33,0.22,1)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=seg, ring_count=rings, radius=r, location=(0,0,0))
    o=bpy.context.active_object; o.name=name
    m=bpy.data.materials.new(name+"_Mat"); m.use_nodes=True
    bsdf=m.node_tree.nodes.get("Principled BSDF"); bsdf.inputs["Base Color"].default_value=color; bsdf.inputs["Roughness"].default_value=0.85
    o.data.materials.append(m); return o
def add_rot(o, secs, axis='Z', start=1):
    fps=bpy.context.scene.render.fps; endf=start+int(secs*fps); o.rotation_mode='XYZ'
    o.keyframe_insert(data_path="rotation_euler", frame=start)
    rot=[0,0,0]; idx={'X':0,'Y':1,'Z':2}[axis]; rot[idx]=math.radians(360); o.rotation_euler=rot
    o.keyframe_insert(data_path="rotation_euler", frame=endf)
    for fcu in o.animation_data.action.fcurves:
        for kp in fcu.keyframe_points: kp.interpolation='LINEAR'
    bpy.context.scene.frame_start=start; bpy.context.scene.frame_end=endf
def add_orbit(empty, secs, start=1):
    fps=bpy.context.scene.render.fps; endf=start+int(secs*fps); empty.rotation_mode='XYZ'
    empty.keyframe_insert(data_path="rotation_euler", frame=start)
    empty.rotation_euler=(0,0,math.radians(360)); empty.keyframe_insert(data_path="rotation_euler", frame=endf)
    for fcu in empty.animation_data.action.fcurves:
        for kp in fcu.keyframe_points: kp.interpolation='LINEAR'
    bpy.context.scene.frame_start=start; bpy.context.scene.frame_end=endf
def main():
    clear_scene()
    mars=create_uv_sphere("Mars",1.0,64,32,(0.76,0.33,0.22,1)); add_rot(mars,60,'Z',1)
    ph_e=bpy.data.objects.new("Phobos_Orbit",None); bpy.context.collection.objects.link(ph_e)
    ph=create_uv_sphere("Phobos",0.12,24,12,(0.71,0.59,0.55,1)); ph.parent=ph_e; ph.location.x=2.0; add_orbit(ph_e,12,1)
    de_e=bpy.data.objects.new("Deimos_Orbit",None); bpy.context.collection.objects.link(de_e)
    de=create_uv_sphere("Deimos",0.08,24,12,(0.78,0.70,0.66,1)); de.parent=de_e; de.location.x=3.2; add_orbit(de_e,20,1)
if __name__=="__main__": main(); print("Exporte como GLB (File > Export > glTF 2.0)") 
