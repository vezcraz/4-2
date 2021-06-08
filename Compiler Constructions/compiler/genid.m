fid=fopen("inputfile.txt","w");
y0=2003;
ytot=18;
degrees={ "B1", "B2", "B3", "B4", "B5", "A1", "A3", "A4", "A7", "A8", "AA" };
psts={ "PS", "TS" };
if(!exist("total"))
	total = 1000;
end
alphanums=[ 10, 44, 46, 48:59, 65:90, 97:122 ];
l=100*randi(100,1,total)./randi(1000,1,total);
for n=1:total
  x=char(alphanums(randi(67,1,l(n))));
	year=2003+randi(18);
	d1=degrees{randi(11)};
	d2=degrees{randi(11)};
	if(d2==d1)
		d2=psts{randi(2)};
	end
	fprintf(fid,"%s %d%s%s%04dG ",x,year,d1,d2,randi(1099));
	if(randi(2)-1) fprintf(fid,"\n"); end
end
fprintf(fid,"\n");
fclose(fid);
