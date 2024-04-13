from manim import * 

class CreateCircle(Scene):
    def construct(self):
        # Create input layer circles
        input_layer_circles = VGroup(
            Circle(radius=0.5, color=RED),
            Circle(radius=0.5, color=RED)
        ).arrange(DOWN, buff=0.5)
        
    # Create input layer labels
        input_layer_labels = VGroup(
            Text("2", font_size=20).move_to(
                input_layer_circles[0].get_center()),
            Text("3", font_size=20).move_to(
                input_layer_circles[1].get_center())
        )
        
    # Create input layer title
        input_title = Text("Input Layer", font_size=20).move_to(UP * 3)

        # Add input layer elements to the scene
        self.add(input_layer_circles, input_layer_labels, input_title)

        # Create hidden layer circles