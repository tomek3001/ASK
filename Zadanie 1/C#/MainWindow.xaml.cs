using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Microsoft.Win32;
using System.Diagnostics;

namespace zadanie1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        int new_command_length = 0;

        public int ALVal
        {
            get { return (int)GetValue(ALValProperty);  }
            set { SetValue(ALValProperty, value);  }

        }

        public static readonly DependencyProperty ALValProperty =
            DependencyProperty.Register("ALVal", typeof(int), typeof(MainWindow));

        public MainWindow()
        {
            InitializeComponent();
            this.DataContext = this;
            this.ALVal = 0;
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }

        private void RunButton_Click(object sender, RoutedEventArgs e)
        {
            string przycisk = "";
            if (ADDButton.IsChecked == true)
                przycisk = "ADD";
            else if (SUBButton.IsChecked == true)
                przycisk = "SUB";
            else if (MOVButton.IsChecked == true)
                przycisk = "MOV";
            
            OutputTextBox.Text = "Wciśnięty został przycisk RUN, a wybrana operacja to " + przycisk +
                ", podczas gdy argument pierwszy to " + ARG1Val.Text + ", a argument drugi to " + ARG2Val.Text + ".";
        }

        private void StepButton_Click(object sender, RoutedEventArgs e)
        {
            string przycisk = "";
            if (ADDButton.IsChecked == true)
                przycisk = "ADD";
            else if (SUBButton.IsChecked == true)
                przycisk = "SUB";
            else if (MOVButton.IsChecked == true)
                przycisk = "MOV";
            OutputTextBox.Text = "Wciśnięty został przycisk STEP, a wybrana operacja to " + przycisk + 
                ", podczas gdy argument pierwszy to " + ARG1Val.Text + ", a argument drugi to " + ARG2Val.Text + ".";
        }

        private void ClearButton_Click(object sender, RoutedEventArgs e)
        {
            //string przycisk = "";
            //if (ADDButton.IsChecked == true)
            //    przycisk = "ADD";
            //else if (SUBButton.IsChecked == true)
            //    przycisk = "SUB";
            //else if (MOVButton.IsChecked == true)
            //    przycisk = "MOV";
            //OutputTextBox.Text = "Wciśnięty został przycisk CLEAR, a wybrana operacja to " + przycisk +
            //    ", podczas gdy argument pierwszy to " + ARG1Val.Text + ", a argument drugi to " + ARG2Val.Text + ".";

            OutputTextBox.Text = "";
        }

        private void ComboBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        { 
            int original_length = OutputTextBox.Text.Length;
            string przycisk = "";
            if (ADDButton.IsChecked == true)
                przycisk = "ADD";
            else if (SUBButton.IsChecked == true)
                przycisk = "SUB";
            else if (MOVButton.IsChecked == true)
                przycisk = "MOV";

            OutputTextBox.Text = OutputTextBox.Text + przycisk + " " + ARG1Val.Text + "," + ARG2Val.Text + "\n";
            new_command_length = OutputTextBox.Text.Length - original_length;
            this.DataContext = this;
            this.ALVal = 110;
        }

        private void Button_Click_1(object sender, RoutedEventArgs e)
        {
            if (OutputTextBox.Text.Length - new_command_length >= 0)
                OutputTextBox.Text = OutputTextBox.Text.Remove(OutputTextBox.Text.Length - new_command_length);
        }

        private void SaveButton_Click(object sender, RoutedEventArgs e)
        {
            string path = @"D:\Tomek\Szkoła\Semestr 6\Architektura Systemów Komputerowych\Projekty\Zadanie 1\zadanie1\code.txt";
            File.WriteAllText(path, OutputTextBox.Text);
            MessageBox.Show("Succesfully saved.");
        }

        private void LoadButton_Click(object sender, RoutedEventArgs e)
        {
            string path = @"D:\Tomek\Szkoła\Semestr 6\Architektura Systemów Komputerowych\Projekty\Zadanie 1\zadanie1\code.txt";
            OutputTextBox.Text = File.ReadAllText(path);

        }

        private void ARG1Val_TextChanged(object sender, TextChangedEventArgs e)
        {

        }
    }
}