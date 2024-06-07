import customtkinter as ctk
import CTkTable as ctkTab
import AlgoritmaDP as DynamicProg
import AlgoritmaGreedy as GR

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Knapsack City Building")
        self.geometry("1024x766")
        self.dataset= []
        self.weightWood = 0
        self.weightStone = 0
        self.weightSteel = 0
        self.prodRatio = 0
        self.popRatio = 0
        self.weights = []
        self.profits = []
        self.n = len(self.dataset)

        self.dpResult = []
        self.dpResource = []
        self.dpProfit = []
        self.dpTime = 0
        self.dpMemory = 0

        self.greedy = []
        self.grResource = []
        self.grProfit = []
        self.GreedyTag = ""
        self.grTime = 0
        self.grMemory = 0

        
    
    def change_page(self, current_page, next_page):
        print("Change page")
        match(next_page):
            case "Start Memu":
                print("To Menu")
                current_page.pack_forget()
                current_page.destroy()
                menu = StartMenu(self)
            case "Input Data":
                print("to input")
                self.reset()
                current_page.pack_forget()
                current_page.destroy()
                input_data = InputData(self)
            case "Greedy":
                print("To greedy")
                self.processData()
                current_page.pack_forget()
                current_page.destroy()
                greedy = GreedyUI(self)
            case "DP":
                print("To DP")
                current_page.pack_forget()
                current_page.destroy()
                DP = DPGUI(self)
            case "Result":
                print("To Result")
                current_page.pack_forget()
                current_page.destroy()
                Result = ResultUI(self)
    
    def reset(self):
        self.dataset= []
        self.weightWood = 0
        self.weightStone = 0
        self.weightSteel = 0
        self.prodRatio = 0
        self.popRatio = 0
        self.weights = []
        self.profits = []
        self.n = len(self.dataset)

        self.dpResult = []
        self.dpResource = []
        self.dpProfit = []
        self.dpTime = 0
        self.dpMemory = 0

        self.greedy = []
        self.grResource = []
        self.grProfit = []
        self.GreedyTag = ""
        self.grTime = 0
        self.grMemory = 0

    def processData(self):
        for i in range(len(self.dataset)):
            weight = (int(self.dataset[i][1]), int(self.dataset[i][2]), int(self.dataset[i][3]))
            profit = (int(self.dataset[i][4]),int(self.dataset[i][5]))

            profit = (profit[0] * self.prodRatio, profit[1] * self.popRatio)

            self.weights.append(weight)
            self.profits.append(profit)
        
        self.n = len(self.dataset)


class StartMenu(ctk.CTkFrame):
    def __init__(self, master):
        members = "By:\nMohammad Argo G. P. (1301220003)\nNail Yusra A. Z. (1301220504)\nAkhtar Muhammad A. (1301223087)"
        super().__init__(master)
        self.pack(padx=10, pady=10, fill='both', expand=True)

        title = ctk.CTkLabel(self,text="Knapsack City Building", font=("Ariel", 60))
        title.pack(padx=10, pady=20, fill='x', expand=True)

        member = ctk.CTkLabel(self, text=members, font=("Ariel", 30))
        member.pack(padx=10, pady=20, fill='x', expand=True)

        str_btn = ctk.CTkButton(self, text="Start", width=268, height=78, font=("Ariel", 40), command= lambda : master.change_page(self, "Input Data"))
        str_btn.pack(padx=10, pady=20)

        qt_btn = ctk.CTkButton(self, text="Quit", width=268, height=78, font=("Ariel", 40),command=master.destroy)
        qt_btn.pack(padx=10, pady=20)

class InputData(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        self.building_list = []
        self.master = master
        super().__init__(master, **kwargs)
        self.pack(fill='both', expand=True)

        resource_frame = ctk.CTkFrame(self)
        resource_frame.pack(side='top',expand=True, fill='x')
        initial_resource = ctk.CTkLabel(resource_frame, text="Initial Resource:", font=("Ariel",40))
        initial_resource.pack(padx=10, pady=20, side='left')

        inpRes = ctk.CTkFrame(self)
        inpRes.pack(side='top',expand=True, fill='x')
        woodFrame = ctk.CTkFrame(inpRes)
        woodFrame.pack(side="left", fill='x')
        wood_txt = ctk.CTkLabel(woodFrame, text="Wood:", font=("Ariel", 32))
        wood_txt.pack(padx=10, pady=5, side='top')
        self.wood_enrty = ctk.CTkEntry(woodFrame, font=("Ariel", 32))
        self.wood_enrty.pack(padx=10, pady=5, side='top')

        stoneFrame = ctk.CTkFrame(inpRes)
        stoneFrame.pack(side="left", fill='x')
        stone_txt = ctk.CTkLabel(stoneFrame, text="Stone:", font=("Ariel", 32))
        stone_txt.pack(padx=10, pady=5, side='top')
        self.stone_enrty = ctk.CTkEntry(stoneFrame, font=("Ariel", 32))
        self.stone_enrty.pack(padx=10, pady=5, side='top')

        steelFrame = ctk.CTkFrame(inpRes)
        steelFrame.pack(side="left", fill='x')
        steel_txt = ctk.CTkLabel(steelFrame, text="Steel:", font=("Ariel", 32))
        steel_txt.pack(padx=10, pady=5, side='top')
        self.steel_enrty = ctk.CTkEntry(steelFrame, font=("Ariel", 32))
        self.steel_enrty.pack(padx=10, pady=5, side='top')

        buildingFrame = ctk.CTkFrame(self)
        buildingFrame.pack(padx=10, pady=20,side="top", fill='x')
        building_txt = ctk.CTkLabel(buildingFrame, text="Building:", font=("Ariel", 40))
        building_txt.grid(padx=10, row=0, column=0, sticky='NW')
        plus_btn = ctk.CTkButton(buildingFrame, text="+", font=("Ariel",40), width=50, height=40, command=self.add_building)
        plus_btn.grid(padx=10, row=0, column=1, sticky='NW')
        
        nextFrame = ctk.CTkFrame(self)
        nextFrame.pack(padx=10, pady=5, side='bottom', fill='x')
        next_btn = ctk.CTkButton(nextFrame, text="Next ►", font=("Ariel", 40), command=lambda : self.changePage(master))
        next_btn.pack(padx=10, pady=10, side='right')
        
        ratioFrame = ctk.CTkFrame(self)
        ratioFrame.pack(padx=10, pady=5, side='bottom', fill='x')

        productionFrame = ctk.CTkFrame(ratioFrame)
        productionFrame.pack(padx=10, pady=10, side='left')
        production_txt = ctk.CTkLabel(productionFrame, text="Production:", font=("Ariel", 40))
        production_txt.pack(padx=10, pady=10, side='top')
        self.production_entry = ctk.CTkEntry(productionFrame, font=("Ariel", 32))
        self.production_entry.pack(padx=10, pady=10, side='top')

        devider = ctk.CTkLabel(ratioFrame, text=":", font=("Ariel", 60))
        devider.pack(padx=10, pady=10, side='left')

        populationFrame = ctk.CTkFrame(ratioFrame)
        populationFrame.pack(padx=10, pady=10, side='left')
        population_txt = ctk.CTkLabel(populationFrame, text="Population:", font=("Ariel", 40))
        population_txt.pack(padx=10, pady=10, side='top')
        self.population_entry = ctk.CTkEntry(populationFrame, font=("Ariel", 32))
        self.population_entry.pack(padx=10, pady=10, side='top')


        scaleFrame = ctk.CTkFrame(self)
        scaleFrame.pack(padx=10, pady=5, side='bottom', fill='x')
        scale_resource = ctk.CTkLabel(scaleFrame, text="Profit Scale:", font=("Ariel",40))
        scale_resource.pack(padx=10, side='left', fill='x')

        
        self.add_building()
        

        

    def add_building(self):
            buffer = ctk.CTkFrame(self)
            buffer.pack(pady=3, side="top", fill='x')
            buildingFrame = ctk.CTkFrame(buffer)
            buildingFrame.pack(padx=10, pady=10,side="left")
            name_txt = ctk.CTkLabel(buildingFrame, text="Name: ", font=("Ariel",32))
            name_txt.grid(padx=10, pady=10, row=0, column=0, sticky='NW')
            name_entry = ctk.CTkEntry(buildingFrame, font=("Ariel",32))
            name_entry.grid(padx=10, pady=10, row=0, column=1)
            min_btn = ctk.CTkButton(buildingFrame, text="-", font=("Ariel",40), width=50, height=40, command=lambda: self.remove_building(buffer, building))
            min_btn.grid(padx=10, row=0, column=2, sticky='E')

            woodFrame = ctk.CTkFrame(buildingFrame)
            woodFrame.grid(padx=10, pady=10, row=1, column=0, sticky='W')
            wood_txt = ctk.CTkLabel(woodFrame, text="Wood:", font=("Ariel",32))
            wood_txt.pack(padx=10, pady=5, side='top')
            wood_entry = ctk.CTkEntry(woodFrame, font=('Ariel', 32))
            wood_entry.pack(padx=10, pady=5, side='top')

            stoneFrame = ctk.CTkFrame(buildingFrame)
            stoneFrame.grid(padx=10, pady=10, row=1, column=1, sticky='W')
            stone_txt = ctk.CTkLabel(stoneFrame, text="Stone:", font=("Ariel",32))
            stone_txt.pack(padx=10, pady=5, side='top')
            stone_entry = ctk.CTkEntry(stoneFrame, font=('Ariel', 32))
            stone_entry.pack(padx=10, pady=5, side='top')

            steelFrame = ctk.CTkFrame(buildingFrame)
            steelFrame.grid(padx=10, pady=10, row=1, column=2, sticky='W')
            steel_txt = ctk.CTkLabel(steelFrame, text="Steel:", font=("Ariel",32))
            steel_txt.pack(padx=10, pady=5, side='top')
            steel_entry = ctk.CTkEntry(steelFrame, font=('Ariel', 32))
            steel_entry.pack(padx=10, pady=5, side='top')

            productionFrame = ctk.CTkFrame(buildingFrame)
            productionFrame.grid(padx=10, pady=10, row=2, column=0, sticky='W')
            production_txt = ctk.CTkLabel(productionFrame, text="Production:", font=("Ariel",32))
            production_txt.pack(padx=10, pady=5, side='top')
            production_entry = ctk.CTkEntry(productionFrame, font=('Ariel', 32))
            production_entry.pack(padx=10, pady=5, side='top')

            populationFrame = ctk.CTkFrame(buildingFrame)
            populationFrame.grid(padx=10, pady=10, row=2, column=1, sticky='W')
            population_txt = ctk.CTkLabel(populationFrame, text="Population:", font=("Ariel",32))
            population_txt.pack(padx=10, pady=5, side='top')
            population_entry = ctk.CTkEntry(populationFrame, font=('Ariel', 32))
            population_entry.pack(padx=10, pady=5, side='top')

            building = []
            building.append(name_entry)
            building.append(wood_entry)
            building.append(stone_entry)
            building.append(steel_entry)
            building.append(production_entry)
            building.append(population_entry)
            self.building_list.append(building)
            self.update_data(self.master)
    
    def remove_building(self, item, building):
        item.destroy()
        self.building_list.remove(building)
        self.update_data(self.master)
       

    def print_result(self):
        buildings = self.building_list
        result = []
        for building in buildings:
            name = building[0].get()
            wood = building[1].get()
            stone = building[2].get()
            steel = building[3].get()
            production = building[4].get()
            population = building[5].get()

            result.append((name, wood, stone, steel, production, population))
        return result
    
    def update_data(self, master):
        master.weightWood = int(self.wood_enrty.get())
        master.weightStone = int(self.stone_enrty.get())
        master.weightSteel = int(self.steel_enrty.get())
        master.prodRatio = float(self.production_entry.get())
        master.popRatio = float(self.population_entry.get())
        new_data = self.print_result()
        master.dataset = new_data
    
    def changePage(self, master):
        self.update_data(master)
        master.change_page(self,"Greedy")
        
class GreedyUI(ctk.CTkScrollableFrame):
    def __init__(self,  master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill='both', expand=True)
        
        self.grWeight = []
        self.grWResource = [0, 0, 0]
        self.grWProfit = [0, 0]
        self.wTime = 0
        self.wMem = 0

        self.grProfit = []
        self.grPResource = [0, 0, 0]
        self.grPProfit = [0, 0]
        self.pTime = 0
        self.pMem = 0

        self.grDensity = []
        self.grDResource = [0, 0, 0]
        self.grDProfit = [0, 0]
        self.dTime = 0
        self.dMem = 0

        self.getItem(master)

        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.pack(padx=10, pady=10, side='top', fill='x')
        back_btn = ctk.CTkButton(buttonFrame, text="◄ Back", font=('Ariel', 32), command=lambda : master.change_page(self, "Input Data"))
        back_btn.pack(padx=10, pady=10, side='left')
        DP_btn = ctk.CTkButton(buttonFrame, text="DP ►", font=('Ariel', 32), command= lambda : master.change_page(self, "DP"))
        DP_btn.pack(padx=10, pady=10, side='right')


        costBuffer = ctk.CTkFrame(self)
        costBuffer.pack(padx=10, pady=10, side='top', fill='x')
        costFrame = ctk.CTkFrame(costBuffer)
        costFrame.pack(padx=10, pady=10, side='top', fill='x')
        cost_txt = ctk.CTkLabel(costFrame, padx=10, pady=10, text="Greedy by Cost", font=('Ariel', 32), anchor='w')
        cost_txt.pack(padx=10, pady=10, side='top')
        costTabFrame = ctk.CTkFrame(costFrame)
        costTabFrame.pack(padx=10, pady=10, side='top', fill='x')
        costTable = Table(costTabFrame, self.grWeight)

        costResult = ctk.CTkFrame(costFrame)
        costResult.pack(padx=10, pady=10, side='bottom', fill='x')
        costResource = ResourceUsed(costResult, self.grWResource)
        costProfit = TotalProfit(costResult, self.grWProfit)
        costPerformance = PerformanceMetrics(costResult, [self.wTime, self.wMem])

        profitBuffer = ctk.CTkFrame(self)
        profitBuffer.pack(padx=10, pady=10, side='top', fill='x')
        profitFrame = ctk.CTkFrame(profitBuffer)
        profitFrame.pack(padx=10, pady=10, side='top', fill='x')
        profit_txt = ctk.CTkLabel(profitFrame, padx=10, pady=10, text="Greedy by Profit", font=('Ariel', 32), anchor='w')
        profit_txt.pack(padx=10, pady=10, side='top')
        profitTabFrame = ctk.CTkFrame(profitFrame)
        profitTabFrame.pack(padx=10, pady=10, side='top', fill='x')
        profitTable = Table(profitTabFrame, self.grProfit)

        profitResult = ctk.CTkFrame(profitFrame)
        profitResult.pack(padx=10, pady=10, side='bottom', fill='x')
        profitResource = ResourceUsed(profitResult, self.grPResource)
        profitProfit = TotalProfit(profitResult, self.grPProfit)
        profitPerformance = PerformanceMetrics(profitResult, [self.pTime, self.pMem])

        densityBuffer = ctk.CTkFrame(self)
        densityBuffer.pack(padx=10, pady=10, side='top', fill='x')
        densityFrame = ctk.CTkFrame(densityBuffer)
        densityFrame.pack(padx=10, pady=10, side='top', fill='x')
        density_txt = ctk.CTkLabel(densityFrame, padx=10, pady=10, text="Greedy by Density", font=('Ariel', 32), anchor='w')
        density_txt.pack(padx=10, pady=10, side='top')
        densityTabFrame = ctk.CTkFrame(densityFrame)
        densityTabFrame.pack(padx=10, pady=10, side='top', fill='x')
        densityTable = Table(densityTabFrame, self.grDensity)
        
        densityResult = ctk.CTkFrame(densityFrame)
        densityResult.pack(padx=10, pady=10, side='bottom', fill='x')
        densityResource = ResourceUsed(densityResult, self.grDResource)
        densityProfit = TotalProfit(densityResult, self.grDProfit)
        densityPerformance = PerformanceMetrics(densityResult, [self.pTime, self.pMem])

        self.bestProfit(master)
    
    def getItem(self, master):
        capacity = (master.weightWood, master.weightStone, master.weightSteel)
        weightPicked, self.wTime, self.wMem = GR.greed_byWeight(master.weights, master.profits, capacity)
        profitPicked, self.pTime, self.pMem = GR.greed_byProfit(master.weights, master.profits, capacity, [master.prodRatio, master.popRatio])
        densityPicked, self.dTime, self.dMem = GR.greed_byDensity(master.weights, master.profits, capacity, [master.prodRatio, master.popRatio])

        for i in weightPicked:
            item = master.dataset[i]
            self.grWResource[0] += int(item[1])
            self.grWResource[1] += int(item[2])
            self.grWResource[2] += int(item[3])
            self.grWProfit[0] += int(item[4])
            self.grWProfit[1] += int(item[5])
            self.grWeight.append(item)

        for i in profitPicked:
            item = master.dataset[i]
            self.grPResource[0] += int(item[1])
            self.grPResource[1] += int(item[2])
            self.grPResource[2] += int(item[3])
            self.grPProfit[0] += int(item[4])
            self.grPProfit[1] += int(item[5])
            self.grProfit.append(item)
        
        for i in densityPicked:
            item = master.dataset[i]
            self.grDResource[0] += int(item[1])
            self.grDResource[1] += int(item[2])
            self.grDResource[2] += int(item[3])
            self.grDProfit[0] += int(item[4])
            self.grDProfit[1] += int(item[5])
            self.grDensity.append(item)
    
    def bestProfit(self, master):
        profitW = GR.calculateProfit(self.grWProfit[0], self.grWProfit[1], master.prodRatio, master.popRatio)
        profitP = GR.calculateProfit(self.grPProfit[0], self.grPProfit[1], master.prodRatio, master.popRatio)
        profitD = GR.calculateProfit(self.grDProfit[0], self.grDProfit[1], master.prodRatio, master.popRatio)

        best = max(profitW, profitP, profitD)
        if best == profitW:
            master.greedy = self.grWeight
            master.grResource = self.grWResource
            master.grProfit = self.grWProfit
            master.GreedyTag = "Weight"
            master.grTime = self.wTime
            master.grMemory = self.wMem

        elif best == profitP:
            master.greedy = self.grProfit
            master.grResource = self.grPResource
            master.grProfit = self.grPProfit
            master.GreedyTag = "Profit"
            master.grTime = self.pTime
            master.grMemory = self.pMem

        elif best == profitD:
            master.greedy = self.grDensity
            master.grResource = self.grDResource
            master.grProfit = self.grDProfit
            master.GreedyTag = "Density"
            master.grTime = self.dTime
            master.grMemory = self.dMem


class DPGUI(ctk.CTkScrollableFrame):
    def __init__(self,  master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill='both', expand=True)
        self.itemsPicked = []
        self.itemTable = []
        self.resource = [0, 0, 0]
        self.profit = [0, 0]
        self.time = 0
        self.memory = 0

        self.getItems(master)
        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.pack(padx=10, pady=10, side='top', fill='x')
        back_btn = ctk.CTkButton(buttonFrame, text="◄ Back", font=('Ariel', 32), command=lambda : master.change_page(self, "Greedy"))
        back_btn.pack(padx=10, pady=10, side='left')
        DP_btn = ctk.CTkButton(buttonFrame, text="Result ►", font=('Ariel', 32), command= lambda : master.change_page(self, "Result"))
        DP_btn.pack(padx=10, pady=10, side='right')

        DPBuffer = ctk.CTkFrame(self)
        DPBuffer.pack(padx=10, pady=10, side='top', fill='x')
        DPFrame = ctk.CTkFrame(DPBuffer)
        DPFrame.pack(padx=10, pady=10, side='top', fill='x')
        DP_txt = ctk.CTkLabel(DPFrame, padx=10, pady=10, text="Dynamic Programming", font=('Ariel', 32), anchor='w')
        DP_txt.pack(padx=10, pady=10, side='top')
        DPTabFrame = ctk.CTkFrame(DPFrame)
        DPTabFrame.pack(padx=10, pady=10, side='top', fill='x')
        DPTable = Table(DPTabFrame, self.itemTable)

        DPResult = ctk.CTkFrame(DPFrame)
        DPResult.pack(padx=10, pady=10, side='bottom', fill='x')
        DPResource = ResourceUsed(DPResult, self.resource)
        DPProfit = TotalProfit(DPResult, self.profit)
        DPPerformance = PerformanceMetrics(DPResult, [self.time, self.memory])
        
        master.dpResult = self.itemTable
        master.dpResource = self.resource
        master.dpProfit = self.profit
        master.dpTime = self.time
        master.dpMemory = self.memory

    
    def getItems(self, master):
        max_profit, self.itemsPicked, self.time, self.memory = DynamicProg.unbounded_knapsack(master.n, master.weightWood, master.weightStone, master.weightSteel,
                                                                 master.weights, master.profits, [master.prodRatio, master.popRatio])
        for i in self.itemsPicked:
            item = master.dataset[i]
            self.resource[0] += int(item[1])
            self.resource[1] += int(item[2])
            self.resource[2] += int(item[3])
            self.profit[0] += int(item[4])
            self.profit[1] += int(item[5])
            self.itemTable.append(item)



class ResultUI(ctk.CTkScrollableFrame):
    def __init__(self,  master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill='both', expand=True)

        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.pack(padx=10, pady=10, side='top', fill='x')
        back_btn = ctk.CTkButton(buttonFrame, text="◄ Back", font=('Ariel', 32), command=lambda : master.change_page(self, "DP"))
        back_btn.pack(padx=10, pady=10, side='left')
        DP_btn = ctk.CTkButton(buttonFrame, text="Menu ►", font=('Ariel', 32), command= lambda : master.change_page(self, "Start Memu"))
        DP_btn.pack(padx=10, pady=10, side='right')

        GreedyBuffer = ctk.CTkFrame(self)
        GreedyBuffer.pack(padx=10, pady=10, side='top', fill='x')
        GreedyFrame = ctk.CTkFrame(GreedyBuffer)
        GreedyFrame.pack(padx=10, pady=10, side='top', fill='x')
        Greedy_txt = ctk.CTkLabel(GreedyFrame, padx=10, pady=10, text="Greedy by " + master.GreedyTag, font=('Ariel', 32), anchor='w')
        Greedy_txt.pack(padx=10, pady=10, side='top')
        GreedyTabFrame = ctk.CTkFrame(GreedyFrame)
        GreedyTabFrame.pack(padx=10, pady=10, side='top', fill='x')
        GreedyTable = Table(GreedyTabFrame, master.greedy)

        GreedyResult = ctk.CTkFrame(GreedyFrame)
        GreedyResult.pack(padx=10, pady=10, side='bottom', fill='x')
        GreedyResource = ResourceUsed(GreedyResult, master.grResource)
        GreedyProfit = TotalProfit(GreedyResult, master.grProfit)
        GreedyPerformance = PerformanceMetrics(GreedyResult, [master.grTime, master.grMemory])

        DPBuffer = ctk.CTkFrame(self)
        DPBuffer.pack(padx=10, pady=10, side='top', fill='x')
        DPFrame = ctk.CTkFrame(DPBuffer)
        DPFrame.pack(padx=10, pady=10, side='top', fill='x')
        DP_txt = ctk.CTkLabel(DPFrame, padx=10, pady=10, text="Dynamic Programming", font=('Ariel', 32), anchor='w')
        DP_txt.pack(padx=10, pady=10, side='top')
        DPTabFrame = ctk.CTkFrame(DPFrame)
        DPTabFrame.pack(padx=10, pady=10, side='top', fill='x')
        DPTable = Table(DPTabFrame, master.dpResult)

        DPResult = ctk.CTkFrame(DPFrame)
        DPResult.pack(padx=10, pady=10, side='bottom', fill='x')
        DPResource = ResourceUsed(DPResult, master.dpResource)
        DPProfit = TotalProfit(DPResult, master.dpProfit)
        DPPerformance = PerformanceMetrics(DPResult, [master.dpTime, master.dpMemory])

class ResourceUsed(ctk.CTkFrame):
    def __init__(self, master, data) -> None:
        super().__init__(master, width=268, height=169)
        self.pack(padx=10, pady=10, side='left')

        costRes_txt = ctk.CTkLabel(self, padx=10, pady=10, text="Resource used:", font=('Ariel', 24))
        costRes_txt.pack(padx=3, pady=5, side='top')

        valueFrame = ctk.CTkFrame(self)
        valueFrame.pack(padx=10, pady=5, side='top', anchor='w')
        wood_txt = ctk.CTkLabel(valueFrame, text="Wood:", padx=3, pady=5, font=('Ariel', 20))
        wood_txt.grid(padx=7, pady=5, row=0, column=0, sticky='NW')
        wood_result = ctk.CTkLabel(valueFrame, text=str(data[0]), padx=3, pady=5, font=('Ariel', 20))
        wood_result.grid(row=0, column=1)
        stone_txt = ctk.CTkLabel(valueFrame, text="Stone:", padx=3, pady=5, font=('Ariel', 20))
        stone_txt.grid(padx=7, pady=5, row=1, column=0, sticky='NW')
        stone_result = ctk.CTkLabel(valueFrame, text=str(data[1]), padx=3, pady=5, font=('Ariel', 20))
        stone_result.grid(row=1, column=1)
        steel_txt = ctk.CTkLabel(valueFrame, text="Steel:", padx=3, pady=5, font=('Ariel', 20))
        steel_txt.grid(padx=7, pady=5, row=2, column=0, sticky='NW')
        steel_result = ctk.CTkLabel(valueFrame, text=str(data[2]), padx=3, pady=5, font=('Ariel', 20))
        steel_result.grid(row=2, column=1)

class TotalProfit(ctk.CTkFrame):
    def __init__(self, master, data) -> None:
        super().__init__(master, width=268, height=169)
        self.pack(padx=10, pady=10, side='left')

        totProf_txt = ctk.CTkLabel(self, padx=10, pady=10, text="Total Profit:", font=('Ariel', 24))
        totProf_txt.pack(padx=3, pady=5, side='top', fill='both')

        valueFrame = ctk.CTkFrame(self)
        valueFrame.pack(padx=10, pady=5, side='top', anchor='w', fill='both')
        prod_txt = ctk.CTkLabel(valueFrame, text="Production:", padx=3, pady=5, font=('Ariel', 20))
        prod_txt.grid(padx=7, pady=5, row=0, column=0, sticky='NW')
        prod_result = ctk.CTkLabel(valueFrame, text=str(data[0]), padx=3, pady=5, font=('Ariel', 20))
        prod_result.grid(row=0, column=1)
        pop_txt = ctk.CTkLabel(valueFrame, text="Population:", padx=3, pady=5, font=('Ariel', 20))
        pop_txt.grid(padx=7, pady=5, row=1, column=0, sticky='NW')
        pop_result = ctk.CTkLabel(valueFrame, text=str(data[1]), padx=3, pady=5, font=('Ariel', 20))
        pop_result.grid(row=1, column=1)

class PerformanceMetrics(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master, width=268, height=169)
        self.pack(padx=10, pady=10, side='left')

        time_txt = ctk.CTkLabel(self, padx=10, pady=10, text="Peformance:", font=('Ariel', 24))
        time_txt.pack(padx=3, pady=5, side='top', fill='both')

        valueFrame = ctk.CTkFrame(self)
        valueFrame.pack(padx=10, pady=5, side='top', anchor='w', fill='both')
        prod_txt = ctk.CTkLabel(valueFrame, text="Run Time:", padx=3, pady=5, font=('Ariel', 20))
        prod_txt.grid(padx=7, pady=5, row=0, column=0, sticky='NW')
        prod_result = ctk.CTkLabel(valueFrame, text=f"{data[0]:.2} ms", padx=3, pady=5, font=('Ariel', 20))
        prod_result.grid(row=0, column=1)
        pop_txt = ctk.CTkLabel(valueFrame, text="Peak Memory:", padx=3, pady=5, font=('Ariel', 20))
        pop_txt.grid(padx=7, pady=5, row=1, column=0, sticky='NW')
        pop_result = ctk.CTkLabel(valueFrame, text=f"{data[1]*10**-6} MB", padx=3, pady=5, font=('Ariel', 20))
        pop_result.grid(row=1, column=1)



class Table:
    def __init__(self, master, data) -> None:
        self.table = [("No.", "Building Name",  "Wood", "Stone", "Steel", "Production", "Population", "Cost")]
        self.processData(data)
        tot_row = len(self.table)
        tot_col = len(self.table[0])

        tab = ctkTab.CTkTable(master, row=tot_row, column=tot_col, values=self.table)
        tab.pack(padx=10, pady=10, side='top', fill='x')


    def processData(self, data):
        for i, item in enumerate(data):
            cost = GR.calculateCost(int(item[1]), int(item[2]), int(item[3]))
            content = (i+1, item[0], item[1], item[2], item[3], item[4], item[5], cost)
            self.table.append(content)
       

if __name__ == "__main__":
    app = App()
    start_menu = StartMenu(app)
    app.mainloop()
