(guest = readline()),
	(host = readline()),
	(result = readline()),
	(guestHost = guest + host),
	(a = guestHost.split("").sort()),
	(b = result.split("").sort()),
	(y = !0),
	(i = 0);
do {
	x = a[i] === b[i];
	i++;
	if (!x) {
		y = !1;
		break;
	}
} while (i <= b.length);
if (!y) print("NO");
else print("YES");
