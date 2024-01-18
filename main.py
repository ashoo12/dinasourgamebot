import pygame

def load_image(file_path):
    return pygame.image.load(file_path)

# Load and resized images
dinosaur = load_image("dinosaur.png")
obstacles_original = load_image("obstacles.png")
size = (100, 100)
obstacles = pygame.transform.scale(obstacles_original, size)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))  # Set the background color (in RGB format)

# Initial position of the dinosaur
dinosaur_x =0
dinosaur_y = 300
# positions of obstacles
obstacles1_x=300
obstacles2_x=600

# Jump variables
jumping = False
jump_count = 10

# Blit images onto the screen
screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
screen.blit(obstacles, (obstacles1_x, 300))
screen.blit(obstacles, (obstacles2_x, 300))

# Update the display
pygame.display.flip()

# Main game loop function
def play_game():
    global dinosaur_x,dinosaur_y,obstacles1_x,obstacles2_x,jumping,jump_count
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check for automatic jump
        dinosaur_x +=10
        if dinosaur_x == obstacles1_x-70 or dinosaur_x==obstacles2_x-70:
            jumping = True
        # Jump logic
        if jumping:
            if jump_count >= -10:
                # Calculate vertical displacement during the jump
                displacement = (jump_count * abs(jump_count)) * 0.5

                dinosaur_y -= displacement
                jump_count -= 1
            else:
                jumping = False
                jump_count = 10  # Reset jump count
# Redraw the screen with the updated position of the dinosaur
        screen.fill((255, 255, 255))
        screen.blit(dinosaur, (dinosaur_x, dinosaur_y))
        screen.blit(obstacles, (obstacles1_x, 300))
        screen.blit(obstacles, (obstacles2_x, 300))
        if dinosaur_x==800:
            dinosaur_x=0
        # Update the display
        pygame.display.flip()
        # Control the frame rate
        pygame.time.Clock().tick(30)
        # Adjust the frames per second (FPS) as needed

play_game()

# Quit Pygame
pygame.quit()
