
# Blender 3.x+ script — gera "mars_system.glb" com animação embutida
# Uso:
# 1) Abrir Blender (v3.6+).
# 2) Scripting > New > colar este script > Run.
# 3) File > Export > glTF 2.0 (.glb) e exportar como "mars_system.glb".
#
# Animações:
# - Marte: rotação 360° em 60 s.
# - Fobos: órbita a 2.0 unidades, 360° em 12 s.
# - Deimos: órbita a 3.2 unidades, 360° em 20 s.
import bpy, math

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_uv_sphere(name, radius, segments=48, rings=24, color=(0.76,0.33,0.22,1)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=radius, location=(0,0,0))
    obj = bpy.context.active_object
    obj.name = name
    mat = bpy.data.materials.new(name + "_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    bsdf.inputs["Roughness"].default_value = 0.85
    obj.data.materials.append(mat)
    return obj

def add_rotation_anim(obj, seconds, axis='Z', start=1):
    fps = bpy.context.scene.render.fps
    endf = start + int(seconds*fps)
    obj.rotation_mode = 'XYZ'
    obj.keyframe_insert(data_path="rotation_euler", frame=start)
    rot = [0.0, 0.0, 0.0]
    axis_idx = {'X':0,'Y':1,'Z':2}[axis]
    rot[axis_idx] = math.radians(360.0)
    obj.rotation_euler = rot
    obj.keyframe_insert(data_path="rotation_euler", frame=endf)
    for fcu in obj.animation_data.action.fcurves:
        for kp in fcu.keyframe_points:
            kp.interpolation = 'LINEAR'
    bpy.context.scene.frame_start = start
    bpy.context.scene.frame_end = endf

def add_orbit_anim(empty, seconds, radius, start=1):
    fps = bpy.context.scene.render.fps
    endf = start + int(seconds*fps)
    empty.rotation_mode = 'XYZ'
    empty.keyframe_insert(data_path="rotation_euler", frame=start)
    empty.rotation_euler = (0, 0, math.radians(360.0))
    empty.keyframe_insert(data_path="rotation_euler", frame=endf)
    for fcu in empty.animation_data.action.fcurves:
        for kp in fcu.keyframe_points:
            kp.interpolation = 'LINEAR'
    bpy.context.scene.frame_start = start
    bpy.context.scene.frame_end = endf

def main():
    clear_scene()
    mars = create_uv_sphere("Mars", radius=1.0, segments=64, rings=32, color=(0.76,0.33,0.22,1))
    add_rotation_anim(mars, seconds=60.0, axis='Z', start=1)

    phobos_empty = bpy.data.objects.new("Phobos_Orbit", None)
    bpy.context.collection.objects.link(phobos_empty)
    phobos = create_uv_sphere("Phobos", radius=0.12, segments=24, rings=12, color=(0.71,0.59,0.55,1))
    phobos.parent = phobos_empty
    phobos.location.x = 2.0
    add_orbit_anim(phobos_empty, seconds=12.0, radius=2.0, start=1)

    deimos_empty = bpy.data.objects.new("Deimos_Orbit", None)
    bpy.context.collection.objects.link(deimos_empty)
    deimos = create_uv_sphere("Deimos", radius=0.08, segments=24, rings=12, color=(0.78,0.70,0.66,1))
    deimos.parent = deimos_empty
    deimos.location.x = 3.2
    add_orbit_anim(deimos_empty, seconds=20.0, radius=3.2, start=1)

    mars.name = "Mars"; phobos.name = "Phobos"; deimos.name = "Deimos"
    for obj in [phobos_empty, deimos_empty]:
        obj.location = (0,0,0)

if __name__ == "__main__":
    main()
    print("Cena criada. Exporte como GLB: File > Export > glTF 2.0 (.glb)")
