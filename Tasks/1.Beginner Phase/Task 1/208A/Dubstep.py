remix  = input()

words = remix.split('WUB')

words = [word for word in words if word != '']    # to remove ''

original_song = ' '.join(words)

print(original_song)




