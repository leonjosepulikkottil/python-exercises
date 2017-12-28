#! /bin/python
import click

@click.command()
@click.option('--sum', nargs=2, type=float)
@click.option('--sub', nargs=2, type=float)
@click.option('--mult', nargs=2, type=float)
@click.option('--divi', nargs=2, type=float)

def smpcalc(sum,sub,mult,divi):
	if sum and not sub and not mult and not divi: # if --add
		print (sum[0]+sum[1]) 
	elif sub and not sum and not mult and not divi:# if --sub
		print (sub[0]-sub[1])
	elif mult and not sum and not sub and not divi:# if --mult
		print (mult[0]*mult[1])
	elif divi and not sum and not sub and not mult:# if --divi
		print (divi[0]/divi[1])

if __name__ == '__main__':
    pass
   