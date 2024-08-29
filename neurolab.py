import matplotlib.pyplot as plt
import matplotlib
import numpy as np

colors_hex = [
    "#FF6347", "#4682B4", "#32CD32", "#FFD700", "#DC143C",
    "#1E90FF", "#DAA520", "#FF69B4", "#A0522D", "#8A2BE2",
    "#00FA9A", "#FF4500", "#DA70D6", "#EEE8AA", "#98FB98",
    "#AFEEEE", "#DB7093", "#F4A460", "#2E8B57", "#C71585",
    "#FFA07A", "#20B2AA", "#778899", "#B0C4DE", "#FFFF54",
    "#FFDAB9", "#CD5C5C", "#F08080", "#3CB371", "#40E0D0",
    "#66CDAA", "#BA55D3", "#9370DB", "#3B9C9C", "#7B68EE",
    "#00FF7F", "#BDB76B", "#6B8E23", "#556B2F", "#FFA500",
]

def remap_partitions(partitions, mapping):
    """Remap community indices according to a specified mapping dictionary."""
    new_partitions = {}
    for node, community in partitions.items():
        new_partitions[node] = mapping.get(community, community)
    return new_partitions

def calculate_node_strengths(G):
    """Calculate the total strength for each node in the graph."""
    return {node: sum(data['weight'] for _, _, data in G.edges(node, data=True)) for node in G.nodes()}

def get_adjacency_matrix(mapper):
    """Extract the adjacency matrix from a UMAP mapper object."""
    adjacency_matrix = np.zeros(mapper.graph_.shape)
    index_pointer = 0
    for i in range(adjacency_matrix.shape[0]):
        row_length = mapper.graph_.indptr[i+1] - mapper.graph_.indptr[i]
        adjacency_matrix[i, mapper.graph_.indices[index_pointer:index_pointer+row_length]] = mapper.graph_.data[index_pointer:index_pointer+row_length]
        index_pointer += row_length
    return adjacency_matrix

def plot_raster(raster, fps, markersize=5):
    """Plot a raster plot of neuronal activity over time."""
    num_neurons, num_frames = raster.shape
    plt.figure(figsize=(12, 6))

    # Plot neuron firing events
    ax = plt.axes((0.05, 0.35, 0.75, 0.6))
    indices = np.where(raster == 1)
    plt.plot(indices[1], indices[0] + 1, marker='|', linestyle='None', markersize=markersize, color='black')
    ax.set_xlim(0, num_frames-1)
    ax.set_ylim(1, num_neurons)
    plt.xticks([])
    plt.ylabel("Neuron Label")

    # Plot coactivity over time
    ax = plt.axes((0.05, 0.12, 0.75, 0.2))
    coactivity = np.sum(raster, axis=0)
    time = np.arange(0, num_frames) / (fps * 60)
    plt.plot(time, coactivity, linewidth=0.5, color='black')
    ax.set_xlim(min(time), max(time))
    ax.set_ylim(0, max(coactivity) + 1)
    plt.xlabel("Time (min)")
    plt.ylabel("Coactivity")

    # Plot neuron activity levels
    ax = plt.axes((0.85, 0.35, 0.1, 0.6))
    activity = np.sum(raster, axis=1)
    plt.plot(activity, np.arange(1, num_neurons + 1), color='black', linewidth=1)
    ax.set_xlim(0, max(activity) + 1)
    ax.set_ylim(1, num_neurons)
    plt.xlabel("Activity")
    plt.yticks([])

def surrogate_raster(real_raster):
    """Generate a surrogate raster by permuting the firing times of each neuron."""
    return np.apply_along_axis(np.random.permutation, axis=1, arr=real_raster)

def plot_cluster_raster(raster, fps, partition, markersize=5):
    """Plot a raster plot with neurons grouped by their cluster membership."""
    cluster_indices = np.array(list(partition.values()))
    num_neurons, num_frames = raster.shape
    activity = np.zeros(num_neurons)  # Initialize activity array for each neuron

    plt.figure(figsize=(12, 6))

    ax = plt.axes((0.05, 0.35, 0.75, 0.6))
    count = 0
    num_colors = len(colors_hex)
    for cluster_id in range(max(cluster_indices) + 1):
        indices_in_cluster = np.where(cluster_indices == cluster_id)[0]
        color = colors_hex[cluster_id % num_colors]
        for i in indices_in_cluster:
            indices = np.where(raster[i, :] == 1)[0]
            plt.plot(indices, raster[i, indices] * (count + 1), marker='|', linestyle='None', markersize=markersize, color=color)
            activity[count] = np.sum(raster[i, :])  # Calculate activity for each neuron
            count += 1
    ax.set_xlim(0, num_frames - 1)
    ax.set_ylim(1, num_neurons)
    plt.xticks([])
    plt.ylabel("Neuron Label")

    ax = plt.axes((0.05, 0.12, 0.75, 0.2))
    coactivity = np.sum(raster, axis=0)
    time = np.arange(0, num_frames) / (fps * 60)
    plt.plot(time, coactivity, linewidth=0.5, color='black')
    ax.set_xlim(min(time), max(time))
    ax.set_ylim(0, max(coactivity) + 1)
    plt.xlabel("Time (min)")
    plt.ylabel("Coactivity")

    ax = plt.axes((0.85, 0.35, 0.1, 0.6))
    plt.plot(activity, np.arange(1, num_neurons + 1), color='black', linewidth=1)
    ax.set_xlim(0, max(activity) + 1)
    ax.set_ylim(1, num_neurons)
    plt.xlabel("# Frames")
    plt.yticks([])