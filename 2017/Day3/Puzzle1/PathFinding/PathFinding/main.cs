using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace PathFinding
{
    class Day3
    {
        private List<Vertex> nodes;
        private List<Edge> edges;
        private HashSet<Vertex> settledNodes;
        private HashSet<Vertex> unsettledNodes;
        private Dictionary<Vertex, Vertex> predecessors;
        private Dictionary<Vertex, int> distance;

        public Day3(List<Vertex> nodes, List<Edge> edges)
        {
            this.nodes = nodes;
            this.edges = edges;
        }

        public void Execute(Vertex source)
        {
            settledNodes = new HashSet<Vertex>();
            unsettledNodes = new HashSet<Vertex>();
            predecessors = new Dictionary<Vertex, Vertex>();
            distance = new Dictionary<Vertex, int>();

            distance.Add(source, 0);
            unsettledNodes.Add(source);
            while(unsettledNodes.Count > 0)
            {
                Vertex node = GetMinimum(unsettledNodes);
                settledNodes.Add(node);
                unsettledNodes.Remove(node);
                FindMinimalDistances(node);
            }
        }

        private Vertex GetMinimum(HashSet<Vertex> vertexes)
        {
            Vertex minimum = null;
            foreach(var vertex in vertexes)
            {
                if(minimum == null)
                {
                    minimum = vertex;
                    continue;
                }

                if(GetShortestDistance(vertex) < GetShortestDistance(minimum))
                {
                    minimum = vertex;
                }
            }

            return minimum;
        }

        private int GetShortestDistance(Vertex destination)
        {
            if(!distance.ContainsKey(destination)) return int.MaxValue;

            return distance[destination];
        }

        private void FindMinimalDistances(Vertex node)
        {
            List<Vertex> adjacentNodes = GetNeighbours(node);
            foreach(Vertex target in adjacentNodes)
            {
                if(GetShortestDistance(target) > GetShortestDistance(node) + GetDistance(node, target))
                {
                    distance.Add(target, GetShortestDistance(node) + GetDistance(node, target));
                    predecessors.Add(target, node);
                    unsettledNodes.Add(target);
                }
            }
        }

        private int GetDistance(Vertex node, Vertex target)
        {
            // foreach(var edge in edges)
            // {
            //     if(edge.Source == node && edge.Destination == target)
            //     {
            //         return edge.Weight;
            //     }
            // }

            return 1;
        }

        private List<Vertex> GetNeighbours(Vertex node)
        {
            var neighbours = new List<Vertex>();
            foreach(var edge in edges)
            {
                if(edge.Source == node && !settledNodes.Contains(edge.Destination))
                {
                    neighbours.Add(edge.Destination);
                }
            }
            return neighbours;
        }

        public List<Vertex> GetPath(Vertex target)
        {
            var path = new List<Vertex>();
            Vertex step = target;
            if(!predecessors.ContainsKey(step))
            {
                return null;
            }

            path.Add(step);

            while(predecessors.ContainsKey(step))
            {
                step = predecessors[step];
                path.Add(step);
            }

            path.Reverse();

            return path;
        }

        static int input = 347991;

        static void Main(string[] args)
        {
            //int input = 347991;
            int length = (int)Math.Ceiling(Math.Sqrt(input)) + 2;

            var grid = new Vertex[length][];
            for(int i = 0; i < grid.Length; ++i)
            {
                grid[i] = new Vertex[length];
            }

            var nodes = new List<Vertex>();
            var edges = new List<Edge>();

            int xPos = length / 2;
            int yPos = length / 2;

            int number = 1;
            int increment = 1;
            while(number < (length * length))
            {
                Fill(grid, ref number, ref xPos, ref yPos, 1, 0, increment);
                Fill(grid, ref number, ref xPos, ref yPos, 0, -1, increment);
                ++increment;
                Fill(grid, ref number, ref xPos, ref yPos, -1, 0, increment);
                Fill(grid, ref number, ref xPos, ref yPos, 0, 1, increment);
                ++increment;
            }

            for(int x = 0; x < grid.Length; ++x)
            {
                for(int y = 0; y < grid[x].Length; ++y)
                {
                    if(grid[x][y] == null) continue;

                    nodes.Add(grid[x][y]);

                    if(x > 0 && grid[x - 1][y] != null)
                    {
                        edges.Add(new Edge($"Edge_{x}_{y}", grid[x][y], grid[x - 1][y]));
                    }
                    if(y > 0 && grid[x][y - 1] != null)
                    {
                        edges.Add(new Edge($"Edge_{x}_{y}", grid[x][y], grid[x][y - 1]));
                    }
                    if(x < grid.Length - 1 && grid[x + 1][y] != null)
                    {
                        edges.Add(new Edge($"Edge_{x}_{y}", grid[x][y], grid[x + 1][y]));
                    }
                    if(y < grid[x].Length - 1 && grid[x][y + 1] != null)
                    {
                        edges.Add(new Edge($"Edge_{x}_{y}", grid[x][y], grid[x][y + 1]));
                    }
                }
            }

            // for(int i = 0; i < 11; ++i)
            // {
            //     var vertex = new Vertex($"Node_{i}", $"Node_{i}");
            //     nodes.Add(vertex);
            // }

            // void AddLane(string laneID, int source, int dest)
            // {
            //     var edge = new Edge(laneID, nodes[source], nodes[dest]);
            //     edges.Add(edge);
            // }

            // AddLane("Edge_0", 0, 1);
            // AddLane("Edge_1", 0, 2);
            // AddLane("Edge_2", 0, 4);
            // AddLane("Edge_3", 2, 6);
            // AddLane("Edge_4", 2, 7);
            // AddLane("Edge_5", 3, 7);
            // AddLane("Edge_6", 5, 8);
            // AddLane("Edge_7", 8, 9);
            // AddLane("Edge_8", 7, 9);
            // AddLane("Edge_9", 4, 9);
            // AddLane("Edge_10", 9, 10);
            // AddLane("Edge_11", 3, 10);

            Vertex source = null;
            foreach(var vertex in nodes)
            {
                if(vertex == null || vertex.ID != input) continue;

                source = vertex;
                break;
            }

            Debug.Assert(source != null);

            var day = new Day3(nodes, edges);
            day.Execute(source);
            var path = day.GetPath(grid[length / 2][length / 2]);

            foreach(var vertex in path)
            {
                Console.WriteLine(vertex.Name);
            }

            Console.WriteLine($"Path length: {path.Count}");
            Console.WriteLine("Done!");
        }

        static void Fill(Vertex[][] grid, ref int number, ref int xPos, ref int yPos, int xIncrement, int yIncrement, int count)
        {
            for(int i = 0; i < count; ++i)
            {
                int x = xPos + xIncrement * i;
                int y = yPos + yIncrement * i;
                if(x < 0 || y < 0 || x >= grid.Length || y >= grid[0].Length) break;

                if(number + i == input) Console.WriteLine("Here!");
                //Console.WriteLine(number + i);

                grid[xPos + xIncrement * i][yPos + yIncrement * i] = new Vertex(number + i, $"Node_{number + i}");
            }

            number += count;
            xPos += xIncrement * count;
            yPos += yIncrement * count;
        }
    }
}