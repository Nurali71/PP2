import pygame
import config

# Initialize fonts
pygame.font.init()
FONT = pygame.font.SysFont("Arial", 24)
BIG_FONT = pygame.font.SysFont("Arial", 48)
BOLD_FONT = pygame.font.SysFont("Arial", 24, bold=True)

def draw_text(screen, text, x, y, font=FONT, color=config.TEXT_COLOR):
    """Helper function to render text on the screen"""
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def button(screen, text, x, y, w, h, mouse):
    """Draws a button that changes color on hover and returns its Rect"""
    rect = pygame.Rect(x, y, w, h)
    # Check if mouse is over the button
    color = config.BUTTON_HOVER if rect.collidepoint(mouse) else config.BUTTON_COLOR
    
    pygame.draw.rect(screen, color, rect, border_radius=10)
    # Center text inside button
    draw_text(screen, text, x + 20, y + 10, font=FONT, color=(255, 255, 255))
    
    return rect

def main_menu(screen, username):
    """Main Menu screen with username input display"""
    screen.fill(config.BACKGROUND)
    draw_text(screen, "SNAKE ARCHIVE", 150, 80, BIG_FONT, (0, 255, 0))
    
    # Display username input area
    draw_text(screen, "Enter Username:", 210, 180, FONT, (200, 200, 200))
    # Draw a simple box for the name
    input_rect = pygame.Rect(180, 210, 240, 40)
    pygame.draw.rect(screen, (50, 50, 50), input_rect, border_radius=5)
    draw_text(screen, username + "_", 190, 215, BOLD_FONT, (255, 255, 0))

    mouse = pygame.mouse.get_pos()
    
    # Return dict of rects for click detection in main.py
    return {
        "play": button(screen, "Play Game", 210, 280, 180, 50, mouse),
        "leader": button(screen, "Top Scores", 210, 340, 180, 50, mouse),
        "quit": button(screen, "Exit", 210, 400, 180, 50, mouse)
    }

def draw_leaderboard(screen, scores):
    """Draws the Top 10 scores from the database"""
    screen.fill(config.BACKGROUND)
    draw_text(screen, "GLOBAL LEADERBOARD", 160, 50, BOLD_FONT, (0, 255, 255))
    
    # Headers
    draw_text(screen, "User", 100, 120, FONT, (150, 150, 150))
    draw_text(screen, "Score", 300, 120, FONT, (150, 150, 150))
    draw_text(screen, "Level", 450, 120, FONT, (150, 150, 150))
    
    # List top 10 results
    y_offset = 160
    for i, row in enumerate(scores):
        color = (255, 255, 255) if i > 0 else (255, 215, 0) # Gold for #1
        draw_text(screen, f"{i+1}. {row[0]}", 100, y_offset, FONT, color) # Username
        draw_text(screen, str(row[1]), 300, y_offset, FONT, color)        # Score
        draw_text(screen, str(row[2]), 450, y_offset, FONT, color)        # Level
        y_offset += 35
        
    draw_text(screen, "Press ESC to return", 200, 550, FONT, (100, 100, 100))

def game_over_screen(screen, score, level):
    """Static Game Over screen overlay"""
    # Create a semi-transparent surface
    overlay = pygame.Surface((config.WIDTH, config.HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    
    draw_text(screen, "COLD BLOODED MURDER", 120, 200, BIG_FONT, (255, 0, 0))
    draw_text(screen, f"Final Score: {score}", 240, 280, FONT)
    draw_text(screen, f"Level Reached: {level}", 240, 310, FONT)
    draw_text(screen, "Click anywhere to restart", 190, 450, FONT, (100, 100, 100))