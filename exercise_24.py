print("Let's practice everything")
print("'You\'d need to know \'bout escapes with \\ that do:")
print('\n newlines and \t tabs')
poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition 
and requires an explanation
\n\t\where there is none.
"""
print("-------------------")
print(poem)
print("-------------------")

five=10-2+3-6
print(f"This should be five: {five}")
def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans, jars, crates
start_point=10000
beans, jars, creates=secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))