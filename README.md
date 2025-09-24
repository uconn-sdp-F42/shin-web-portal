## IMPORTANT

.gitignore does not include the data files since the size of these files are too large!

## Goal
Find a mapping for a single cell (merfish) to scRNAseq top 5cells closest to the single cell

## Data Notes
### Merfish
```
adjusted_cell_id
ex. ID23009MEDWB_C0021_S1_P0059

donorid(not real) + cell_id + section_number + position
```

`ID23009MEDWB`
- Donor's unique ID
`C0021`
- Cell count
- indicated by `cell_id`
`S1`
- Section
	- section has 60 partitions
- indicated by `section_number`
`P0059`
- Partition
	- partitions start at 0
	- partition has ~60 cells
- indicated by `position`

donor -> section -> partition -> cells

```
donorid(not real) + cell_id + section_number + position
```
