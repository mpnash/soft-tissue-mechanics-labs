$model = 1

gfx read node "model${model}.part0.exnode";
gfx read elem "model${model}.part0.exelem";

# define deformed geometry and pressure
gfx define field "deformed_geom" component Dependent.1 Dependent.2 Dependent.3

# display deformed geometry
gfx define faces egroup "Region"

gfx modify g_element Region general clear circle_discretization 6 default_coordinate Geometry element_discretization "16*16*16" native_discretization none;
gfx modify g_element Region lines coordinate deformed_geom line_width 2 select_on material red selected_material default_selected;
gfx modify g_element Region lines line_width 2 select_on material green selected_material default_selected;
gfx modify g_element Region node_points glyph point general size "1*1*1" centre 0,0,0 font default label cmiss_number select_on material green selected_material default_selected;
gfx modify g_element Region node_points coordinate deformed_geom glyph point general size "1*1*1" centre 0,0,0 font default label cmiss_number select_on material red selected_material default_selected;

#Open graphics window
gfx create window
gfx create axes length 2 material black
gfx draw axes
gfx modify window 1 background colour 1,1,1
gfx modify window 1 layout orthographic width 600 height 600

gfx edit scene
gfx modify window 1 set antialias 2

