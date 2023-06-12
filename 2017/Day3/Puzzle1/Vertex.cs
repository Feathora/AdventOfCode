namespace Day3
{
    public class Vertex
    {
        public int ID
        {
            get; private set;
        }

        public string Name
        {
            get; private set;
        }

        public Vertex(int id, string name)
        {
            ID = id;
            Name = name;
        }
    }
}