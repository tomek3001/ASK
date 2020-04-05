using System;

namespace zadanie1
{
	public class Register
	{
		public string name;
		public int dataH = 0b00000000;
		public int dataL = 0b00000000;
		public int Read(bool high_part)
		{
			if (high_part)
			{
				return dataH;
			}
			return dataL;
		}

		public void Write(bool high_part, int value)
		{
			if (high_part)
			{
				dataH = value;
			}
			else
			{
				dataL = value;
			}
		}
	}
	public class Operations
	{
		public void move(Register source, Register destination, bool from_high, bool to_high)
		{
			int val1 = source.Read(from_high);
			destination.Write(to_high, val1);
		}

		public int add(Register source1, Register source2, Register destination, bool adding = true)
		{
			int val1 = connetct(source1);
			int val2 = connetct(source2);
			int result;
			if (adding)
			{
				result = val1 + val2;
			}
			else
			{
				if (val1 > val2)
				{
					result = val1 - val2;
				}
				else
				{
					result = val2;
					// Ponieważ chcemy to widzieć w jakimś oknie to możemy przesyłać na przykład wartość -1 i wtedy
					// wiemy, że coś skopane jest bo za duża wartość i wypisać, że nie obsługujemy ujemnych
					Console.WriteLine("Brak obsługi liczb ujemnych");
					return -1;
				}
			}
			if (result > 65535)
			{
				Console.WriteLine("Suma jest za duża");
				return -2;
			}
			else
			{
				string binary = Convert.ToString(result, 2).PadLeft(16, '0');
				string first = binary.Substring(0, (int)(binary.Length / 2));
				string last = binary.Substring((int)(binary.Length / 2), (int)(binary.Length / 2));

				val1 = Convert.ToInt32(last, 2);
				val2 = Convert.ToInt32(first, 2);

				destination.Write(false, val1);
				destination.Write(true, val2);
				return 0;
			}
		}
		// Funkcja która służy do złączenia w DUŻĄ liczbę 
		public int connetct(Register temp)
		{
			int value = temp.dataH * 256 + temp.dataL;
			return value;
		}
		public void intToRegister(string from, Register destination)
		{
			int end = from.Length;
			string sub = from.Substring(0, end);
			int num;
			int.TryParse(sub, out num);
			string binary = Convert.ToString(num, 2).PadLeft(16, '0');
			var first = binary.Substring(0, (int)(binary.Length / 2));
			var last = binary.Substring((int)(binary.Length / 2), (int)(binary.Length / 2));
			int val1 = Convert.ToInt32(last, 2);
			int val2 = Convert.ToInt32(first, 2);
			destination.Write(false, val1);
			destination.Write(true, val2);
		}
	}
}