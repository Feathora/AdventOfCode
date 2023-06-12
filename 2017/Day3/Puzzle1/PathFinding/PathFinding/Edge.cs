namespace PathFinding
{
    public class Edge
    {
        public string ID
        {
            get; private set;
        }

        public Vertex Source
        {
            get; private set;
        }

        public Vertex Destination
        {
            get; private set;
        }

        public Edge(string id, Vertex sourceVertex, Vertex destinationVertex)
        {
            ID = id;
            Source = sourceVertex;
            Destination = destinationVertex;
        }
    }
}