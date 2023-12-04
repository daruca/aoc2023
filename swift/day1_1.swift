import SwiftUI

@main
struct MyApp: App {
    @State private var fileContent: String?

    var body: some Scene {
        WindowGroup {
            ContentView()
            Picker(selection: /*@START_MENU_TOKEN@*/.constant(1)/*@END_MENU_TOKEN@*/, label: /*@START_MENU_TOKEN@*/Text("Picker")/*@END_MENU_TOKEN@*/) {
                Text("Day 1 Part 1").tag(1)
                Text("Day 1 Part 2").tag(2)
                Text("Day 2 Part 1").tag(3)
                Text("Day 2 Part 2").tag(4)
            }
            Button("Day 1 Part 1"){
                d11()
            }
            
        }
    }
    
    func d11() {
    }

    
    
}
