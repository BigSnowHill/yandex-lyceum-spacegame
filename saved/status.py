def minimap():
    x_f, y_f = floor_group.sprites()[0].rect.x, floor_group.sprites()[0].rect.y
    x_p, y_p = player.rect.x, player.rect.y
    mini_width = tile_width * 2 // tiles_x
    mini_height = tile_height * 2 // tiles_y
    sc = pygame.surface.Surface((200, 200))
    with open(f'saved/maps/{MAPS[system_Number]}.txt', 'r', encoding='utf-8') as mapFile:
        cur_map = [list(s) for s in mapFile.read().strip().split('\n')]
        for planet in planets.keys():
            if planets[planet]['known']:
                x, y = [int(n) for n in planet.split()]
                planet_type = cur_map[y][x]
                if planet_type == '1':
                    pygame.draw.circle(sc, (0, 22, 213), ((x + 1) * 4, (y + 1) * 4), 5)
                elif planet_type == '0':
                    pygame.draw.circle(sc, (254, 136, 2), ((x + 1) * 4, (y + 1) * 4), 7)
                elif planet_type == '2':
                    pygame.draw.circle(sc, (85, 201, 180), ((x + 1) * 4, (y + 1) * 4), 9)
    pygame.draw.circle(sc, (255, 255, 0), (101, 101), 10)
    pygame.draw.circle(sc, (255, 255, 255), (101, 101), 10, 1)
    x, y = abs((x_f - x_p) // 100), abs((y_f - y_p) // 100)
    if pygame.sprite.spritecollideany(player, floor_group):
        pygame.draw.rect(sc, (255, 255, 255), ((x - 1) * 4, (y - 1) * 4, 4, 4))
    pygame.draw.rect(sc, (255, 255, 255), (0, 0, 200, 200), 1)
    screen.blit(sc, (0, height - 200))