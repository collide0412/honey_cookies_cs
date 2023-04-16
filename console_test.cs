using System;
using System.Windows.Forms;
 
namespace MyApplication
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
 
        private void Form1_Load(object sender, EventArgs e)
        {
            // Display a pop-up with three buttons
            DialogResult result = MessageBox.Show("Please press one of the following buttons:",
                "Popup with Buttons",
                MessageBoxButtons.YesNoCancel,
                MessageBoxIcon.Question);
 
            // Handle the button presses
            if (result == DialogResult.Yes)
            {
                MessageBox.Show("You pressed button A1");
            }
            else if (result == DialogResult.No)
            {
                MessageBox.Show("You pressed button A2");
            }
            else if (result == DialogResult.Cancel)
            {
                MessageBox.Show("You pressed button A3");
            }
        }
    }
}