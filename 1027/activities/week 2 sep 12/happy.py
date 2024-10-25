#Activity 6: Happiness Improver
"""
sad => happy
bad => good
cry => sing
failed => passed
"""

text = input("Input your text: ")
text = text.replace('sad', 'happy')
text = text.replace('bad', 'good')
text = text.replace('cry', 'sing')
text = text.replace('failed', 'passed')

print(text)