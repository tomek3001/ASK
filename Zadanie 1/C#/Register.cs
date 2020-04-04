using System;
namespace zadanie1
{
	public class Register
	{
		public int dataH = 0b00000001;
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

		public void add(Register source1, Register source2,Register destination, 
			bool from_high1, bool from_high2, bool to_high,bool adding = true)
		{
			int val1 = source1.Read(from_high1);
			int val2 = source2.Read(from_high2);
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
					result = destination.Read(to_high);
					// Ponieważ chcemy to widzieć w jakimś oknie to możemy przesyłać na przykład wartość -1 i wtedy
					// wiemy, że coś skopane jest bo za duża wartość i wypisać, że nie obsługujemy ujemnych
					Console.WriteLine("Action is Imposible");
				}
			}
			destination.Write(to_high, result);
		}


	}
}